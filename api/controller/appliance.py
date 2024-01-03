
from sqlalchemy.orm import  Session
from api.controller.depends import get_db
from main import app
from fastapi import Depends, HTTPException
from api.schemas.appliance import AddApplianceRequestBody, DeleteAppliance
from main import app
from data_access.crud.crud_appliance import appliance_Manager


@app.post("/appliance")

def create_appliance(request: AddApplianceRequestBody, db: Session = Depends(get_db)):
    
    #check if household has appliance records
    appliance_records = appliance_Manager.get_multi(db=db, id=request.email)
    if appliance_records:
        print(appliance_records)
        request.seq_num = len(appliance_records) + 1
    else:
        request.seq_num = 1
        
    
    new_appliance = appliance_Manager.createAppliance(db=db, obj_in=request)
    
    return new_appliance
