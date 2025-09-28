from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.database import Activity, User
from ..models.schemas import (
    EmissionCalculationRequest, 
    EmissionCalculationResponse,
    UserCreate,
    UserResponse,
    ActivityResponse
)
from ..services.emission_service import emission_service

router = APIRouter(prefix="/api/emissions", tags=["emissions"])

@router.get("/activities")
async def get_all_activities():
    """Get all available activities organized by category"""
    return emission_service.get_all_activities()

@router.get("/categories")
async def get_activity_categories():
    """Get list of all activity categories"""
    return {"categories": emission_service.get_activity_categories()}

@router.post("/calculate", response_model=EmissionCalculationResponse)
async def calculate_emissions(
    request: EmissionCalculationRequest,
    db: Session = Depends(get_db)
):
    """Calculate CO2 emissions for a given activity"""
    
    # Calculate emissions
    result = emission_service.calculate_emissions(request.activity_type, request.quantity)
    
    if not result:
        raise HTTPException(
            status_code=400, 
            detail=f"Activity type '{request.activity_type}' not found"
        )
    
    # Save activity to database if user email is provided
    if request.user_email:
        # Check if user exists, create if not
        user = db.query(User).filter(User.email == request.user_email).first()
        if not user:
            user = User(email=request.user_email)
            db.add(user)
            db.commit()
        
        # Save activity
        activity = Activity(
            user_email=request.user_email,
            activity_type=request.activity_type,
            quantity=request.quantity,
            co2_emissions=result["co2_emissions"]
        )
        db.add(activity)
        db.commit()
    
    return EmissionCalculationResponse(
        activity_type=result["activity_type"],
        quantity=result["quantity"],
        co2_emissions=result["co2_emissions"],
        unit=result["unit"]
    )

@router.get("/history/{email}", response_model=List[ActivityResponse])
async def get_user_history(email: str, db: Session = Depends(get_db)):
    """Get emission calculation history for a user"""
    activities = db.query(Activity).filter(Activity.user_email == email).order_by(Activity.created_at.desc()).limit(50).all()
    return activities