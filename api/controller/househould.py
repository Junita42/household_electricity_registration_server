from typing import Any
from api.schemas.household import AddHouseholdRequestBody, GetHouseholdResponse
from api.server import app

@app.get("/household/{email}", response_model=GetHouseholdResponse)
def get_household_by_email(email: str):
    response = GetHouseholdResponse(email=email, postal='30332', sqft=1000, household_type='single family', offgrid_flag=False)
    return response

@app.post("/household", response_model=GetHouseholdResponse)
def add_household(household: Any):
    """
    Add a new household to the database.
    """

    # added_household: GetHouseholdResponse = GetHouseholdResponse(household.email, household.postal, household.sqft, household.household_type, household.offgrid_flag)
    print(f'added_household_email: {household.email}')
    return GetHouseholdResponse(email=household.email, 
                                postal=household.postal, 
                                sqft=household.sqft, 
                                household_type=household.household_type, 
                                offgrid_flag=household.offgrid_flag)


# @app.get("/verify_email", response_model=verifyEmail)
# def verify_email(email: str):
#     """
#     Verify if an email exists in the Household database.
#     """
#     household = db.query(Household).filter(Household.email == email).first()
#     if not household:
#         raise HTTPException(status_code=404, detail="Email not found")

#     return verifyEmail(email=email)