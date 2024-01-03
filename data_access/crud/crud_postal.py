from sqlalchemy.orm import Session

from data_access.crud.base import CRUDBase

from data_access.models.valid_postal import Valid_Postal
from api.schemas.household import AddHouseholdRequestBody

class CRUDPostal(CRUDBase[Valid_Postal, AddHouseholdRequestBody]):
    def get_postal(self, db: Session, postal: str):
        
        return db.query(self.model).filter(self.model.postal_code == postal).first()
    
postal_Manager = CRUDPostal(Valid_Postal)