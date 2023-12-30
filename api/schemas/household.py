
from enum import Enum
from pydantic import BaseModel
from typing import Optional, List

#1. veryfy email
class VerifyEmail(BaseModel):
    email: str

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
    email: str
    postal: str
    sqft: int
    household_type: HouseholdTypeEnum
    public_utilities: Optional[str]


class HouseholdResponse(BaseModel):
    email: str
    postal: str
    sqft: int
    household_type: HouseholdTypeEnum
    public_utilities: Optional[str]


class DeleteHousehold(BaseModel):
    email: str


