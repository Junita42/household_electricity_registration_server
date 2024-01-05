from data_access.crud.crud_appliance import appliance_Manager
from data_access.crud.crud_power_generator import power_generator_Manager
from sqlalchemy.orm import Session

def appliance_seq_num(db: Session, email_str: str) -> int:
    # Check if household exists
    appliance_records = appliance_Manager.get_multi(db=db, id=email_str)
    if appliance_records:
        return len(appliance_records) + 1
    return 1

def power_generator_seq_num(db: Session, email_str: str) -> int:
    # Check if household exists
    power_generator_records = power_generator_Manager.get_multi(db=db, id=email_str)
    if power_generator_records:
        return len(power_generator_records) + 1
    return 1