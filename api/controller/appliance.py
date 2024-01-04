
from sqlalchemy.orm import  Session
from api.controller.depends import get_db
from main import app
from fastapi import Depends, HTTPException
from api.schemas.appliance import AddApplianceRequestBody, DeleteAppliance, applianceEnum
from main import app
from data_access.crud.crud_appliance import appliance_Manager
from api.utils.appliance_utils import appliance_seq_num
from data_access.crud.crud_air_handler import air_handler_Manager
from data_access.crud.crud_water_heater import water_heater_Manager
from data_access.crud.crud_ac import ac_Manager
from data_access.crud.crud_heater import heater_Manager
from data_access.crud.crud_heat_pump import heat_pump_Manager


@app.post("/appliance")

def create_appliance(request: AddApplianceRequestBody, db: Session = Depends(get_db)):
    try:
    #check if household has appliance records
        request.seq_num = appliance_seq_num(db, request.email)
            
        appliance_Manager.createAppliance(db=db, obj_in=request)
        
        if request.appliance_type == applianceEnum.air_handler.value:
            airHandlerObj = air_handler_Manager.createAirHandler(db=db, obj_in=request)
            print(airHandlerObj)
            if request.EER:
                ac_Manager.createAC(db=db, obj_in=request)
            if request.energy_source:
                heater_Manager.createHeater(db=db, obj_in=request)
            if request.SEER:
                heat_pump_Manager.createHeatPump(db=db, obj_in=request)
                
        else:
            water_heater_Manager.createWaterHeater(db=db, obj_in=request)
            
    
        

        # Construct and return the response
        return {"message": f"{request.email} {request.appliance_type} {request.seq_num} created"}
    
    except Exception as e:
        # Handle exceptions and rollback transactions if necessary
        raise HTTPException(status_code=400, detail=str(e))