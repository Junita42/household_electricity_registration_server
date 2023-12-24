
from pydantic import BaseModel

#1. veryfy email
class VerifyEmail(BaseModel):
    email: str

#2. veryfy postal code
class VerifyPostalCode(BaseModel):
    postal: str

#3. add household 
class AddHouseholdRequestBody(BaseModel):
    email: str
    postal: str
    sqft: int
    household_type: str
    offgrid_flag: bool


class GetHouseholdResponse(BaseModel):
    email: str
    postal: str
    sqft: int
    household_type: str
    offgrid_flag: bool


class DeleteHousehold(BaseModel):
    email: str


