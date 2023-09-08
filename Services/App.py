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
from Services.Models.SignIn import SignIn
from Services.Models.SignUp import SignUp
from Services.Modules.Documents import UploadAllDocuments, UpdateQuoteToPendingReview

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
    }).execute()

    if len(response['data']) == 1:
        [quote] = response['data']
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
                .eq('State', 'PENDING_REVIEW')
                .execute())
    pendingReview = response.data
    for review in pendingReview:
        responseDocuments = (supabase.table('DocumentsQuotes')
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
            'State': 'PENDING_PAY'
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
            'State': 'REJECT_BY_DOCUMENTS'
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
            'State': 'PAY_ACCEPTED'
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


asyncio.run(serve(app, Config.from_mapping(use_reloader=True)))
