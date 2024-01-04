from sqlalchemy.orm import Session


from data_access.crud.base import CRUDBase
from data_access.models.water_heater import Water_Heater
from api.schemas.appliance import AddApplianceRequestBody, DeleteAppliance



class CRUDWaterHeater(CRUDBase[Water_Heater, AddApplianceRequestBody]):
    def createWaterHeater(self, db: Session, *, obj_in: AddApplianceRequestBody) -> Water_Heater:
        
        water_heater_obj = Water_Heater(
            email=obj_in.email,
            seq_num=obj_in.seq_num,
            tank_size=obj_in.tank_size,
            energy_source=obj_in.energy_source,
            current_temp=obj_in.current_temp
        )
        db.add(water_heater_obj)
        db.commit()
        db.refresh(water_heater_obj)
        return water_heater_obj
    def deleteWaterHeater(self, db: Session, *, obj_in: DeleteAppliance) -> Water_Heater:
        water_heater_obj = db.query(Water_Heater).filter(Water_Heater.email == obj_in.email, 
                                                   Water_Heater.seq_num == obj_in.seq_num).first()
        db.delete(water_heater_obj)
        db.commit()
        return water_heater_obj

    
water_heater_Manager = CRUDWaterHeater(Water_Heater)