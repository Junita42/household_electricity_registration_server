from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from data_access.crud.base import CRUDBase
from data_access.models.household import Household
from api.schemas.household import AddHouseholdRequestBody

class CRUDHousehold(CRUDBase[Household, AddHouseholdRequestBody]):
    pass
    
household_Manager = CRUDHousehold(Household)
