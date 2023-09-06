import asyncio
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from hypercorn.asyncio import serve
from hypercorn.config import Config
from supabase_py import Client, create_client

from Services.Models.Quotes import Quotes
from Services.Models.SignIn import SignIn
from Services.Models.SignUp import SignUp

load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_ANON_KEY")
supabase: Client = create_client(url, key)
app = FastAPI()


@app.post("/user/sign-up")
def SignUp(signUp: SignUp):
    response = supabase.auth.sign_up(signUp.email, signUp.password)
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'body': response
    }


@app.post("/user/sign-in")
def SignIn(signIn: SignIn):
    response = supabase.auth.sign_in(signIn.email, signIn.password)
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'body': response
    }


@app.post("/quotes/create")
def CreateQuote(create: Quotes):
    response = supabase.table("Quotes").insert({
        "Name": create.Name,
        "Email": create.Email,
        "NumberPhone": create.NumberPhone,
        "Address": create.Address,
        "Observation": create.Observation,
    }).execute()
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'body': {
            'Inserted': 0,
            'RowAffects': 0,
        }
    }


@app.post("/user/documents/upload/obligatory")
def UploadObligatoryDocuments():
    pass


asyncio.run(serve(app, Config.from_mapping(use_reloader=True)))
