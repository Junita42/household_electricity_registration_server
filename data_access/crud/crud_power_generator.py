from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from data_access.crud.base import CRUDBase
from data_access.models.power_generator import Power_Generator
from api.schemas.power_generator import AddPowerGeneratorRequestBody, DeletePowerGenerator


class CRUDAppliance(CRUDBase[Power_Generator, AddPowerGeneratorRequestBody]):
    def createAppliance(self, db: Session, *, obj_in: AddPowerGeneratorRequestBody) -> Appliance:
        
        appliance_obj = Power_Generator(
            email=obj_in.email,
            seq_num=obj_in.seq_num,
            manufacturer=obj_in.manufacturer.value,
            electricity_model=obj_in.electricity_model,
            BTU = obj_in.BTU,
        )
        db.add(appliance_obj)
        db.commit()
        db.refresh(appliance_obj)
        return appliance_obj
    
    def deleteAppliance(self, db: Session, *, obj_in: DeleteAppliance) -> Appliance:
        appliance_obj = db.query(Appliance).filter(Appliance.email == obj_in.email, 
                                                   Appliance.seq_num == obj_in.seq_num).first()
        db.delete(appliance_obj)
        db.commit()
        return appliance_obj
    
    
appliance_Manager = CRUDAppliance(Appliance)