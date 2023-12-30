from typing import Any
from sqlalchemy.orm import  Session
from api.controller.depends import get_db
from main import app
from fastapi import HTTPException
from api.schemas.household import AddHouseholdRequestBody, HouseholdResponse, VerifyEmail
from main import app
from data_access.models.household import Household

from fastapi import Depends


@app.post('/household', response_model=HouseholdResponse)
async def add_household(household: AddHouseholdRequestBody, db: Session = Depends(get_db)):
    """
    Add a new household to the database.
    """
    # added_household: GetHouseholdResponse = GetHouseholdResponse(household.email, household.postal, household.sqft, household.household_type, household.offgrid_flag)
    print(f'added_household_email: {household.email}')
    # return GetHouseholdResponse(email=household.email, 
    #                             postal=household.postal, 
    #                             sqft=household.sqft, 
    #                             household_type=household.household_type, 
    #                             offgrid_flag=household.offgrid_flag)
    new_household = Household(email=household.email, 
                                postal=household.postal, 
                                sqft=household.sqft, 
                                household_type=household.household_type, 
                                public_utilities=household.public_utilities,)
    db.add(new_household)
    db.commit()
    db.refresh(new_household)
    return new_household


@app.get("/verify_email", response_model=VerifyEmail)
def verify_email(email: str, db: Session = Depends(get_db)):
    """
    Verify if an email exists in the Household database.
    """
    email_existence = db.query(Household).filter(Household.email == email).first()
    if not email_existence:
        raise HTTPException(status_code=404, detail="Email not found")
    return email_existence
    # return VerifyEmail(email=email)

# @app.get("/verify_email", response_model=VerifyEmail)
# def verify_email(email: str):
#     """
#     Verify if an email exists in the Household database.
#     """
#     household = Session.query(Household).filter(Household.email == email).first()
#     if not household:
#         raise HTTPException(status_code=404, detail="Email not found")

#     return VerifyEmail(email=email)

# @app.get("/household/{email}", response_model=GetHouseholdResponse)
# def get_household_by_email(email: str):
#     response = GetHouseholdResponse(email=email, postal='30332', sqft=1000, household_type='single family', offgrid_flag=False)
#     return response

@app.post("/household", response_model=HouseholdResponse)
async def add_household(household: AddHouseholdRequestBody):
    """
    Add a new household to the database.
    """
    

    # added_household: GetHouseholdResponse = GetHouseholdResponse(household.email, household.postal, household.sqft, household.household_type, household.offgrid_flag)
    print(f'added_household_email: {household.email}')
    # return GetHouseholdResponse(email=household.email, 
    #                             postal=household.postal, 
    #                             sqft=household.sqft, 
    #                             household_type=household.household_type, 
    #                             offgrid_flag=household.offgrid_flag)


