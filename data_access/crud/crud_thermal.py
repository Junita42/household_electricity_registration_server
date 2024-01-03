from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from data_access.models.base_model import Base
from typing import TypeVar
from data_access.crud.base import CRUDBase, CreateSchemaType

from data_access.models.thermal import Thermal
from api.schemas.thermal import AddThermalCoolingRequestBody, AddThermalHeatingRequestBody

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)



class CRUDThermalHeating(CRUDBase[Thermal, AddThermalHeatingRequestBody]):
    def create_thermal(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:

        if obj_in.heating:
            heating_obj = Thermal(
                email=obj_in.email,
                thermal_type="heating",
                setting=obj_in.setting
            )
            db.add(heating_obj)
            db.commit()
            db.refresh(heating_obj)
            return heating_obj
        return None
    
class CRUDThermalCooling(CRUDBase[Thermal, AddThermalCoolingRequestBody]):
    def create_thermal(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        
        if obj_in.cooling:
            cooling_obj = Thermal(
                email=obj_in.email,
                thermal_type="cooling",
                setting=obj_in.setting
            )
            db.add(cooling_obj)
            db.commit()
            db.refresh(cooling_obj)
            return cooling_obj
        return None
        
        
    
    
thermal_Heating_Manager = CRUDThermalHeating(Thermal)
thermal_Cooling_Manager = CRUDThermalCooling(Thermal)