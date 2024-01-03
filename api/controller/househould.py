
from sqlalchemy.orm import  Session
from api.controller.depends import get_db
from main import app
from fastapi import HTTPException
from api.schemas.household import CombinedRequestBody, DeleteHousehold
from api.utils.household_utils import verify_household, verify_postal
from main import app
from data_access.crud.crud_household import household_Manager
from data_access.crud.crud_thermal import thermal_Cooling_Manager, thermal_Heating_Manager



from fastapi import Depends




@app.post("/household")
def create_household(request: CombinedRequestBody, db: Session = Depends(get_db)):
    household_data = request.household
    
    household_exist = verify_household(db, household_data.email)

    if household_exist:
        raise HTTPException(status_code=400, detail="Household already exists")
    
    if not verify_postal(db, household_data.postal):
        raise HTTPException(status_code=400, detail="Invalid postal code")

    household_Manager.create(db=db, obj_in=household_data)
    

   

    thermal_cooling_data = request.thermal_cooling
    thermal_Cooling_Manager.create_thermal(db=db, obj_in=thermal_cooling_data)
    
    thermal_heating_data = request.thermal_heating
    thermal_Heating_Manager.create_thermal(db=db, obj_in=thermal_heating_data)
    
    return household_data.email + " created successfully"

@app.delete("/household")

def remove_household(household_request: DeleteHousehold, db: Session = Depends(get_db)):
    household_exist = verify_household(db, household_request.email)
    if not household_exist:
        raise HTTPException(status_code=400, detail="Household does not exist")
    household_Manager.delete(db=db, id=household_request.email)
    return {"message": "Household deleted successfully"}

    
    