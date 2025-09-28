from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.database import User
from ..models.schemas import UserCreate, UserResponse, WeeklyTipRequest
from ..services.email_service import email_service

router = APIRouter(prefix="/api/users", tags=["users"])

@router.post("/subscribe", response_model=UserResponse)
async def subscribe_user(
    user: UserCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """Subscribe a user for weekly carbon reduction tips"""
    
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        if existing_user.is_subscribed:
            raise HTTPException(
                status_code=400,
                detail="User is already subscribed"
            )
        else:
            # Re-subscribe existing user
            existing_user.is_subscribed = True
            db.commit()
            db.refresh(existing_user)
            return existing_user
    
    # Create new user
    db_user = User(email=user.email, is_subscribed=user.is_subscribed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Send welcome email in background
    background_tasks.add_task(email_service.send_welcome_email, user.email)
    
    return db_user

@router.post("/unsubscribe")
async def unsubscribe_user(email: str, db: Session = Depends(get_db)):
    """Unsubscribe a user from weekly tips"""
    
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.is_subscribed = False
    db.commit()
    
    return {"message": "Successfully unsubscribed"}

@router.post("/send-tip")
async def send_weekly_tip(
    request: WeeklyTipRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """Send a weekly tip to a user (for testing purposes)"""
    
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not user.is_subscribed:
        raise HTTPException(status_code=400, detail="User is not subscribed")
    
    # Send tip in background
    background_tasks.add_task(email_service.send_weekly_tip, request.email)
    
    return {"message": "Weekly tip will be sent shortly"}

@router.get("/", response_model=List[UserResponse])
async def get_all_users(db: Session = Depends(get_db)):
    """Get all users (for admin purposes)"""
    users = db.query(User).all()
    return users