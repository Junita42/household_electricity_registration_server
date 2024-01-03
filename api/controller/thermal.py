from api.utils.household_utils import verify_household, verify_postal
from api.schemas.household import AddHouseholdRequestBody
from data_access.crud.crud_thermal import thermal_Manager

from api.controller.depends import get_db
from main import app
from sqlalchemy.orm import Session
from fastapi import Depends


@app.post("/household/thermal")
def create_thermal(household_request: AddHouseholdRequestBody, db: Session = Depends(get_db)):
    household_exist = verify_household(db, household_request.email)
    valid_postal = verify_postal(db, household_request.postal)

    if not household_exist and valid_postal:

        thermal_entity = thermal_Manager.create_thermal(db=db, obj_in=household_request)
        return thermal_entity
    else:
        pass



