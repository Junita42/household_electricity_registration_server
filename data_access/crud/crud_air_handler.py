from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from data_access.crud.base import CRUDBase
from data_access.models.air_handler import Air_Handler
from api.schemas.appliance import AddApplianceRequestBody, DeleteAppliance



class CRUDAirHandler(CRUDBase[Air_Handler, AddApplianceRequestBody]):
    def createAirHandler(self, db: Session, *, obj_in: AddApplianceRequestBody) -> Air_Handler:
        
        air_handler_obj = Air_Handler(
            email=obj_in.email,
            seq_num=obj_in.seq_num,
            RPM=obj_in.RPM,
        )
        db.add(air_handler_obj)
        db.commit()
        db.refresh(air_handler_obj)
        return air_handler_obj
    
    def deleteAirHandler(self, db: Session, *, obj_in: DeleteAppliance) -> Air_Handler:
        air_handler_obj = db.query(Air_Handler).filter(Air_Handler.email == obj_in.email, 
                                                   Air_Handler.seq_num == obj_in.seq_num).first()
        db.delete(air_handler_obj)
        db.commit()
        return air_handler_obj
    
    
air_handler_Manager = CRUDAirHandler(Air_Handler)