from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from data_access.crud.base import CRUDBase
from data_access.models.heat_pump import Heat_Pump
from api.schemas.appliance import AddApplianceRequestBody, DeleteAppliance



class CRUDHeatPump(CRUDBase[Heat_Pump, AddApplianceRequestBody]):
    def createHeatPump(self, db: Session, *, obj_in: AddApplianceRequestBody) -> Heat_Pump:
        
        heat_pump_obj = Heat_Pump(
            email=obj_in.email,
            air_handler_seq_num=obj_in.seq_num,
            SEER=obj_in.SEER,
            HSPF=obj_in.HSPF,
        )
        db.add(heat_pump_obj)
        db.commit()
        db.refresh(heat_pump_obj)
        return heat_pump_obj
    
    def deleteHeatPump(self, db: Session, *, obj_in: DeleteAppliance) -> Heat_Pump:
        heat_pump_obj = db.query(Heat_Pump).filter(Heat_Pump.email == obj_in.email, 
                                                   Heat_Pump.air_handler_seq_num == obj_in.seq_num).first()
        db.delete(heat_pump_obj)
        db.commit()
        return heat_pump_obj
    
heat_pump_Manager = CRUDHeatPump(Heat_Pump)