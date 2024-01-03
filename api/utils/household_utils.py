from data_access.crud.crud_household import household_Manager
from data_access.crud.crud_postal import postal_Manager
from sqlalchemy.orm import Session

def verify_household(db: Session, email_str: str) -> bool:
    # Check if household exists
    household = household_Manager.get(db=db, id=email_str)
    if household is not None:
        return True
    return False

def verify_postal(db:Session, postal: str) -> bool:    # Check if postal code is valid
    postal = postal_Manager.get_postal(db=db, postal=postal)
    if postal is None:
        return False
    return True