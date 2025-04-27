from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import TestCaseCreate, TestCaseOut
from crud import create_case, get_cases, delete_case
from jose import jwt, JWTError
from config import SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/cases", tags=["cases"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user_id(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user_id

@router.post("/", response_model=TestCaseOut)
def create_test_case(case: TestCaseCreate, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    return create_case(db, case, user_id)

@router.get("/", response_model=list[TestCaseOut])
def list_test_cases(user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    return get_cases(db, user_id)

@router.delete("/{case_id}")
def delete_test_case(case_id: int, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    case = delete_case(db, case_id, user_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    return {"msg": "Deleted"}

