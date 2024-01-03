from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from data_access.crud.base import CRUDBase
from data_access.models.air_handler import Air_Handler
from api.schemas.appliance import AddApplianceRequestBody, DeleteAppliance



class CRUDAppliance(CRUDBase[Air_Handler, AddApplianceRequestBody]):
    def creatAppliance(self, db: Session, *, obj_in: AddApplianceRequestBody) -> Appliance:
        
        appliance_obj = Air_Handler(
            email=obj_in.email,
            manufacture=obj_in.manufacturer,
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