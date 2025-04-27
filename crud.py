from sqlalchemy.orm import Session
from models import User, TestCase
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, username: str, password: str):
    hashed_password = pwd_context.hash(password)
    db_user = User(username=username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user

def create_case(db: Session, case_data, user_id: int):
    db_case = TestCase(**case_data.dict(), creator_id=user_id)
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case

def get_cases(db: Session, user_id: int):
    return db.query(TestCase).filter(TestCase.creator_id == user_id).all()

def get_case(db: Session, case_id: int, user_id: int):
    return db.query(TestCase).filter(TestCase.id == case_id, TestCase.creator_id == user_id).first()

def delete_case(db: Session, case_id: int, user_id: int):
    case = get_case(db, case_id, user_id)
    if case:
        db.delete(case)
        db.commit()
    return case
