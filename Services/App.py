import asyncio
import base64
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from hypercorn.asyncio import serve
from hypercorn.config import Config
from supabase import Client, create_client

from Services.Models.Document import Document
from Services.Models.Quote import Quote
from Services.Models.SignIn import SignIn
from Services.Models.SignUp import SignUp

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
def UploadObligatoryDocuments(document: Document):
    response = (supabase.storage.from_('DocumentsQuote')
                .upload('Dummy.PDF', base64.b64decode(document.Base64)))
    if response.status_code == 200:
        return {
            'isBase64Encoded': False,
            'statusCode': 200,
            'body': 'Successful'
        }
    else:
        return {
            'isBase64Encoded': False,
            'statusCode': 403,
            'body': response
        }

asyncio.run(serve(app, Config.from_mapping(use_reloader=True)))
