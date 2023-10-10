from fastapi import FastAPI, HTTPException, Query
from truecallerpy import search_phonenumber
import asyncio
from starlette.middleware.cors import CORSMiddleware

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = FastAPI()

INSTALLATION_ID = os.environ.get("INSTALLATION_ID")

@app.get("/")
def home():
    return {"message":"Health Check Passed!"}

app.add_middleware(CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],)

@app.get("/search")
async def search_truecaller(phone_number: str = Query(..., description="The phone number to be searched")):
    try:
        response = await search_phonenumber(phone_number, "IN", INSTALLATION_ID)
        return {"data": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))