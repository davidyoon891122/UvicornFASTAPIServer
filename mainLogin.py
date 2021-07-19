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

db = []

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


@app.get("/users", response_class=HTMLResponse)
def get_login(request: Request):
    context = {}
    rsUser = []

    print("getLog {}".format(db))
    cnt = 0
    for user in db:
        cnt += 1
        rsUser.append({'counter': cnt, 'userID': user['userID'], 'userPWD': user['userPWD']})
    
    context['request'] = request
    context['rsUser'] = rsUser
    print(context)

    return template.TemplateResponse('enlist_user.html', context)


@app.post("/users")
def create_user(userInfo: UserInfo):
    db.append(userInfo.dict())
    print("after post")
    print(db)
    return db[-1]



@app.post("/login")
def login(userInfo: UserInfo):
    print(userInfo)
    print(resultMessage)
    if userInfo.userID == login_db[0]["userID"]:
        if userInfo.userPWD == login_db[0]["userPWD"]:
            resultMessage.append({
                "result":"true",
                "message":"Hello, Davidyoon",
            })
            return resultMessage[-1]
        else:
            resultMessage.append({
                "result":"false",
                "message":"Please check your password"
            })
            return resultMessage[-1]
    else:
        resultMessage.append({
            "result":"false",
            "message":"Please check your ID"
        })
        return  resultMessage[-1]

@app.get("/loginChecker", response_class=HTMLResponse)
def get_loginInput(request: Request):
    context = {}

    context['request'] = request

    return template.TemplateResponse('enlist_user.html', context)