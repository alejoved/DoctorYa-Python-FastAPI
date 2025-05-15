import os
from fastapi import Depends, HTTPException, status
from fastapi_jwt import JwtAccessBearer, JwtAuthorizationCredentials

from app.common import constants
from app.common.role import Role

access_security = JwtAccessBearer(secret_key=os.getenv("JWT_SECRET"))

def valid_role(role: Role):
    def valid(credentials: JwtAuthorizationCredentials = Depends(access_security)):
        role_currently = credentials["role"]
        if role_currently != role:
            raise HTTPException(
                status_code = status.HTTP_403_FORBIDDEN,
                detail = constants.access_denied
            )
    return valid

def create_token(identification: str, role: Role):
    subject = {"identification": identification, "role": role}
    return access_security.create_access_token(subject=subject)
