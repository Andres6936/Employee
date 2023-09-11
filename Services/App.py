import asyncio
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from hypercorn.asyncio import serve
from hypercorn.config import Config
from supabase import Client, create_client

from Services.Models.DocumentsObligatory import DocumentsObligatory
from Services.Models.Process import Process
from Services.Models.Quote import Quote
from Services.Models.ScheduleService import ScheduleService
from Services.Models.SignIn import SignIn
from Services.Models.SignUp import SignUp
from Services.Modules.Documents import UploadAllDocuments, UpdateQuoteToPendingReview
from Services.Modules.Schedule import UpdateStateOfScheduleService
from Services.States.PlanType import PlanType
from Services.States.QuoteStates import QuoteStates
from Services.States.ServicesState import ServicesState

load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_ANON_KEY")
supabase: Client = create_client(url, key)
app = FastAPI()


@app.post("/user/sign-up")
def SignUp(signUp: SignUp):
    response = supabase.auth.sign_up({
        "email": signUp.email,
        "password": signUp.password
    })
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'body': response
    }


@app.post("/user/sign-in")
def SignIn(signIn: SignIn):
    response = supabase.auth.sign_in_with_password({
        "email": signIn.email,
        "password": signIn.password
    })
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'body': response
    }


@app.post("/quotes/create")
def CreateQuote(create: Quote):
    response = supabase.table("Quotes").insert({
        "Name": create.Name,
        "Email": create.Email,
        "NumberPhone": create.NumberPhone,
        "Address": create.Address,
        "Observation": create.Observation,
        "Value": create.Value,
        # Is needed to validate the body with the defined in the enum
        "Plan": PlanType[create.Plan].name
    }).execute()

    if len(response.data) == 1:
        [quote] = response.data
        return {
            'isBase64Encoded': False,
            'statusCode': 200,
            'body': quote['Process']
        }
    else:
        return {
            'isBase64Encoded': False,
            'statusCode': 403,
            'body': response
        }


@app.post("/user/documents/obligatory")
def UploadObligatoryDocuments(documents: DocumentsObligatory):
    responseCount = (supabase.table('Quotes')
                     .select('*', count='exact')
                     .eq('Process', documents.Process)
                     .execute())
    if responseCount.count == 1:
        responseUpload = UploadAllDocuments(
            supabase, documents.Documents, documents.Process
        )
        if responseUpload['Error']:
            return {
                'isBase64Encoded': False,
                'statusCode': 403,
                'body': responseUpload['Message']
            }
        else:
            return UpdateQuoteToPendingReview(supabase, documents.Process)
    else:
        return {
            'isBase64Encoded': False,
            'statusCode': 403,
            'body': 'Process Not Found'
        }


@app.post("/operator/review/documents/pending")
def ReviewDocumentsPending():
    response = (supabase.table('Quotes')
                .select('*')
                .eq('State', QuoteStates.PENDING_REVIEW.name)
                .execute())
    pendingReview = response.data
    for review in pendingReview:
        responseDocuments = (supabase.table('Documents')
                             .select('*')
                             .eq('Process', review['Process'])
                             .execute())
        review['Documents'] = responseDocuments.data

    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'body': pendingReview
    }


@app.post("/operator/review/documents/approve")
def ReviewDocumentsApprove(process: Process):
    response = (
        supabase.table('Quotes')
        .update({
            'State': QuoteStates.PENDING_PAY.name
        })
        .eq('Process', process.Process)
        .execute())
    if len(response.data) == 1:
        return {
            'isBase64Encoded': False,
            'statusCode': 200,
            'body': 'Successful'
        }
    else:
        return {
            'isBase64Encoded': False,
            'statusCode': 403,
            'body': 'Cannot update the state of Quote'
        }


@app.post("/operator/review/documents/reject")
def ReviewDocumentsReject(process: Process):
    response = (
        supabase.table('Quotes')
        .update({
            'State': QuoteStates.REJECT_BY_DOCUMENTS.name
        })
        .eq('Process', process.Process)
        .execute())
    if len(response.data) == 1:
        return {
            'isBase64Encoded': False,
            'statusCode': 200,
            'body': 'Successful'
        }
    else:
        return {
            'isBase64Encoded': False,
            'statusCode': 403,
            'body': 'Cannot update the state of Quote'
        }


@app.post("/operator/pay/accept")
def AcceptPayOfQuote(process: Process):
    response = (
        supabase.table('Quotes')
        .update({
            'State': QuoteStates.PAY_ACCEPTED.name
        })
        .eq('Process', process.Process)
        .execute())
    if len(response.data) == 1:
        return {
            'isBase64Encoded': False,
            'statusCode': 200,
            'body': 'Successful'
        }
    else:
        return {
            'isBase64Encoded': False,
            'statusCode': 403,
            'body': 'Cannot update the state of Quote'
        }


@app.post("/operator/services/view/unschedule")
def ReviewServicesUnschedule():
    response = (
        supabase.table('Services')
        .select("*")
        .eq('State', ServicesState.UNSCHEDULED.name)
        .execute())
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'body': response.data
    }


@app.post("/operator/services/schedule")
def ScheduleService(schedule: ScheduleService):
    # Verify that the service exist in the registers
    responseExistService = (
        supabase.table("Services")
        .select('*', count='exact')
        .eq('Process', schedule.Service)
        .eq("State", ServicesState.UNSCHEDULED.name)
        .execute())

    responseExistSchedule = (
        supabase.table("Schedule")
        .select('*', count='exact')
        .eq('Service', schedule.Service)
        .execute()
    )

    if responseExistSchedule.count >= 1:
        return {
            'isBase64Encoded': False,
            'statusCode': 201,
            'body': f'The service {schedule.Service} has been already schedule for the date f{schedule.At}'
        }

    if responseExistService.count == 1:
        response = (supabase.table("Schedule").insert({
            'Service': schedule.Service,
            'At': schedule.At,
            'Operator': schedule.Operator,
            'Manifest': schedule.Manifest,
        }).execute())

        if len(response.data) == 1:
            responseUpdate = UpdateStateOfScheduleService(supabase, schedule.Service)
            if responseUpdate['Error']:
                return {
                    'isBase64Encoded': False,
                    'statusCode': 403,
                    'body': responseUpdate['Message']
                }

            [schedule] = response.data
            return {
                'isBase64Encoded': False,
                'statusCode': 200,
                'body': schedule
            }
        else:
            return {
                'isBase64Encoded': False,
                'statusCode': 403,
                'body': 'Cannot insert register in schedule'
            }
    else:
        return {
            'isBase64Encoded': False,
            'statusCode': 404,
            'body': 'Service not exist'
        }


asyncio.run(serve(app, Config.from_mapping(use_reloader=True)))
