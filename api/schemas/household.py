
from enum import Enum
from pydantic import BaseModel, EmailStr
from typing import Optional, List

#1. veryfy email
class VerifyEmail(BaseModel):
    email: EmailStr

#2. veryfy postal code
class VerifyPostalCode(BaseModel):
    postal: str

#3. add household 

class HouseholdTypeEnum(str, Enum):
    townhome = "townhome"
    apartment = "apartment"
    tiny_house = "tiny house"
    condominium = "condominium"
    modular_home = "modular home"
    house = "house"
class AddHouseholdRequestBody(BaseModel):
    email: EmailStr
    postal: str
    sqft: int
    household_type: HouseholdTypeEnum
    public_utilities: str


class HouseholdResponse(BaseModel):
    email: EmailStr
    postal: str
    sqft: int
    household_type: HouseholdTypeEnum
    public_utilities: str


class DeleteHousehold(BaseModel):
    email: EmailStr


