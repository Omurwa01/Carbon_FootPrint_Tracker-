from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class EmissionCalculationRequest(BaseModel):
    activity_type: str
    quantity: float
    user_email: Optional[EmailStr] = None

class EmissionCalculationResponse(BaseModel):
    activity_type: str
    quantity: float
    co2_emissions: float
    unit: str

class UserCreate(BaseModel):
    email: EmailStr
    is_subscribed: bool = True

class UserResponse(BaseModel):
    id: int
    email: str
    is_subscribed: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class ActivityResponse(BaseModel):
    id: int
    user_email: str
    activity_type: str
    quantity: float
    co2_emissions: float
    created_at: datetime
    
    class Config:
        from_attributes = True

class WeeklyTipRequest(BaseModel):
    email: EmailStr