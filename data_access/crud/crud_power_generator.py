from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from data_access.crud.base import CRUDBase
from data_access.models.power_generator import Power_Generator
from api.schemas.power_generator import AddPowerGeneratorRequestBody, DeletePowerGenerator


class CRUDPowerGenerator(CRUDBase[Power_Generator, AddPowerGeneratorRequestBody]):
    def createPowerGenerator(self, db: Session, *, obj_in: AddPowerGeneratorRequestBody) -> Power_Generator:
        
        appliance_obj = Power_Generator(
            email=obj_in.email,
            seq_num=obj_in.seq_num,
            battery_storage=obj_in.battery_storage,
            kilowatt_hours=obj_in.kilowatt_hours,
            energy_source=obj_in.energy_source,
        )
        db.add(appliance_obj)
        db.commit()
        db.refresh(appliance_obj)
        return appliance_obj
    
    def deletePowerGenerator(self, db: Session, *, obj_in: DeletePowerGenerator) -> Power_Generator:
        appliance_obj = db.query(Power_Generator).filter(Power_Generator.email == obj_in.email, 
                                                   Power_Generator.seq_num == obj_in.seq_num).first()
        db.delete(appliance_obj)
        db.commit()
        return appliance_obj
    
    
power_generator_Manager = CRUDPowerGenerator(Power_Generator)