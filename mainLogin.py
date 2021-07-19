from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import requests

app = FastAPI()

login_db = [
    {
    "userID":"davidyoon",
    "userPWD":"test1234",
    },
]

# data Model
class UserInfo(BaseModel):
    userID: str
    userPWD: str

template = Jinja2Templates(directory="templates")

@app.get("/")
def index():
    return {
        "LoginAPI":"test"
    }


@app.get("/login", response_class=HTMLResponse)
def get_login(request: Request):
    context = {}
    return template.TemplateResponse('login_page.html', context)





@app.post("/login")
def login(userInfo: UserInfo):
    if userInfo.userID == login_db[0]["userID"]:
        if userInfo.userPWD == login_db[0]["userPWD"]:
            return {
                "result":"true",
                "message":"Hello, Davidyoon",
            }
        else:
            return {
                "result":"false",
                "message":"Please check your password"
            }
    else:
        return {
            "result":"false",
            "message":"Please check your ID"
        }
