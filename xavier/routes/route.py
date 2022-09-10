from sys import prefix
from fastapi import APIRouter,FastAPI, Depends, HTTPException,Request, Header,Response
# middleware
from fastapi.middleware.cors import CORSMiddleware
import time
from typing import Callable
from fastapi.routing import APIRoute,APIWebSocketRoute
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt
from jose.exceptions import JOSEError

#model

from xavier.app.model.UsersModel import UsersModel

# api auth
from xavier.app.controller.auth.RestApiAuth import restAuth
from xavier.app.controller.ApiPrivileges import restPrivileges

from xavier.app.helper.JwtToken import AuthHandler

auth_handler = AuthHandler()

app = FastAPI()
api_router_guest = APIRouter()
api_router_auth = APIRouter(dependencies=[Depends(auth_handler.auth_wrapper)])

origins = [
    "https://localhost",
    "http://localhost",
    "https://localhost:8000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router_guest.include_router(restAuth)

api_router_auth.include_router(restPrivileges)

app.include_router(api_router_auth,prefix="/api/v1")
app.include_router(api_router_guest,prefix="/api/v1")








