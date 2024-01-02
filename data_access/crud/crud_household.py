from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from data_access.crud.base import CRUDBase
from data_access.models.household import Household
from data_access.models.valid_postal import Valid_Postal
from api.schemas.household import AddHouseholdRequestBody, VerifyPostalCode, VerifyEmail

class CRUDHousehold(CRUDBase[Household, AddHouseholdRequestBody]):
    pass
    
household_Manager = CRUDHousehold(Household)
