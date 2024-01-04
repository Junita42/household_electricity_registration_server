from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from data_access.crud.base import CRUDBase
from data_access.models.heater import Heater
from api.schemas.appliance import AddApplianceRequestBody, DeleteAppliance



class CRUDHeater(CRUDBase[Heater, AddApplianceRequestBody]):
    def createHeater(self, db: Session, *, obj_in: AddApplianceRequestBody) -> Heater:
        
        heater_obj = Heater(
            email=obj_in.email,
            air_handler_seq_num=obj_in.seq_num,
            energy_source=obj_in.energy_source,
        )
        db.add(heater_obj)
        db.commit()
        db.refresh(heater_obj)
        return heater_obj
    
    def deleteHeater(self, db: Session, *, obj_in: DeleteAppliance) -> Heater:
        heater_obj = db.query(Heater).filter(Heater.email == obj_in.email, 
                                                   Heater.air_handler_seq_num == obj_in.seq_num).first()
        db.delete(heater_obj)
        db.commit()
        return heater_obj
    
heater_Manager = CRUDHeater(Heater)