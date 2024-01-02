from typing import Any
from sqlalchemy.orm import  Session
from api.controller.depends import get_db
from main import app
from fastapi import HTTPException
from api.schemas.household import AddHouseholdRequestBody, HouseholdResponse, VerifyEmail, VerifyPostalCode
from main import app
from data_access.models.household import Household
from data_access.crud.crud_household import household_Manager

from fastapi import Depends

def verify_household_and_postal(db: Session, email_str: str, postal_code_str: str) -> bool:
    # Check if household exists
    household = household_Manager.get(db=db, id=email_str)
    if household is not None:
        return False

    # Check if postal code is valid
    postal = household_Manager.get(db=db, id=postal_code_str)
    if postal is None:
        return False

    return True


@app.post("/household/verification")
def verification(email: VerifyEmail, postal_code: VerifyPostalCode, db: Session = Depends(get_db)):
    is_valid = verify_household_and_postal(db, email.email, postal_code.postal)

    if not is_valid:
        raise HTTPException(status_code=400, detail="Invalid household or postal code")

    return {"message": "Verification successful"}


@app.post("/household")
def create_household(household_request: AddHouseholdRequestBody, db: Session = Depends(get_db)):

    if not verify_household_and_postal(db, household_request.email, household_request.postal):
        raise HTTPException(status_code=400, detail="Invalid household or postal code")

    # Create household logic
    new_household = household_Manager.create(db=db, obj_in=household_request)
    return new_household

    
    