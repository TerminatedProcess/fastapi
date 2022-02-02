from jose import JWTError, jwt
from datetime import datetime, timedelta
from .schemas import *
from .database import *
from .models import *
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings as s

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

# SECRET_KEY
# Algorithm
# Expiration time
#SECRET_KEY = "fbd9e9bfff604e9a4400262b621885f598b7cf205e97d8810c3c10daa84c3b98"
SECRET_KEY = s.secret_key
ALGORITHM = s.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = s.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credentials_exceptions):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        payloadid: str = payload.get("user_id")
        
        if payloadid is None:
            raise credentials_exceptions
        
        token_data = TokenData(id=payloadid) # schemas
    except JWTError:
        raise credentials_exceptions
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), 
                     db: Session = Depends(get_db)): # database
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                          detail=f"Could not validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    token = verify_access_token(token, credentials_exception)
    user = db.query(User).filter(User.id == token.id).first() # models
    return user

