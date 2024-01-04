from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from data_access.crud.base import CRUDBase
from data_access.models.ac import AC
from api.schemas.appliance import AddApplianceRequestBody, DeleteAppliance



class CRUDAC(CRUDBase[AC, AddApplianceRequestBody]):
    def createAC(self, db: Session, *, obj_in: AddApplianceRequestBody) -> AC:
        
        ac_obj = AC(
            email=obj_in.email,
            air_handler_seq_num=obj_in.seq_num,
            EER=obj_in.EER,
        )
        db.add(ac_obj)
        db.commit()
        db.refresh(ac_obj)
        return ac_obj
    
    def deleteAC(self, db: Session, *, obj_in: DeleteAppliance) -> AC:
        ac_obj = db.query(AC).filter(AC.email == obj_in.email, 
                                                   AC.air_handler_seq_num == obj_in.seq_num).first()
        db.delete(ac_obj)
        db.commit()
        return ac_obj
    
ac_Manager = CRUDAC(AC)