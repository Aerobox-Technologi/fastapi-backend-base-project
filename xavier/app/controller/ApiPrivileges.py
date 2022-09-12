from datetime import datetime, timedelta
from typing import Union
from fastapi import Depends, FastAPI, HTTPException, status,APIRouter,Form, Request,Response,exception_handlers
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr,ValidationError, validator
from uuid import uuid4
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from datetime import datetime, timedelta
from sqlalchemy.orm import Session, aliased
from xavier.dbconfig.ConnectionDB import Connection

from xavier.app.model.PrivilegesModel import PrivilegesModel,body_privileges,pagination

restPrivileges = APIRouter(prefix="/privileges")

@restPrivileges.get("/")
async def index(body : pagination):
    data = PrivilegesModel.getAllPrivileges(body,10)
    if data['status']==True:
        res = {
            "status":True,
            "message":"success get data",
            "code":200,
            "data":data['data']
        }
        return JSONResponse(content=res, status_code=status.HTTP_200_OK)
    else:
        res={
            "status":False,
            "code":400,
            "message":data['message']
        }
        return JSONResponse(content=res, status_code=status.HTTP_400_BAD_REQUEST)

@restPrivileges.get("/edit/{id}")
async def edit(id : int):
    data = PrivilegesModel.getPrivilegesById(id)
    if(data['status']==True):
        res={
            "status"    :True,
            "code"      :200,
            "message"   :"success get data",
            "data"      :data['data']
        }
        return JSONResponse(content=res, status_code=status.HTTP_200_OK)
    else:
        res={
            "status"  : False,
            "code"    :400,
            "message" : data['message'],
        }
        return JSONResponse(content=res, status_code=status.HTTP_400_BAD_REQUEST)


@restPrivileges.post("/create")
async def create(body: body_privileges):
    try:
        save=PrivilegesModel.createPrivileges(body)
        if save['status']==True:
            res={
                "status":True,
                "code"  : 200,
                "message" : "success save data"
            }
            return JSONResponse(content=res, status_code=status.HTTP_200_OK)
        else:
            res={
                "status":False,
                "code"  : 400,
                "message": "failed save data"
            }
            return JSONResponse(content=res, status_code=status.HTTP_400_BAD_REQUEST)

    except ValidationError as e:
        errMsg = str(e.__dict__['orig'])
        res = {
            "status"  :False,
            "code"    : 400,
            "message" : errMsg
        }

        return JSONResponse(content=res, status_code=status.HTTP_400_BAD_REQUEST)


@restPrivileges.get("/update/{id}")
async def update(body: body_privileges,id : int):
    update = PrivilegesModel.updatePrivileges(body,id)
    if update['status']==True:
        res={
            "status":True,
            "message":"success update data"
        }
        return JSONResponse(content=res, status_code=status.HTTP_200_OK)
    else:
        res={
            "status":False,
            "message":"success update data"
        }
        return JSONResponse(content=res, status_code=status.HTTP_400_BAD_REQUEST)

    
@restPrivileges.get("/delete/{id}")
async def delete(id : int):
    delete = PrivilegesModel.deleteById(id)
    if(delete['status']==True):
        res = {
            "status":True,
            "code" : 200,
            "message" : "success delete data"
        }
        return JSONResponse(content=res, status_code=status.HTTP_200_OK)
    else:
        res = {
            "status" : False,
            "code":400,
            "message": "failed save data"
        }
        return JSONResponse(content=res, status_code=status.HTTP_400_BAD_REQUEST)



