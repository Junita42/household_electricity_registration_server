from sqlalchemy.orm import  Session
from api.controller.depends import get_db
from main import app
from fastapi import Depends, HTTPException
from api.schemas.power_generator import AddPowerGeneratorRequestBody, DeletePowerGenerator, EnergySourceEnum
from data_access.crud.crud_power_generator import power_generator_Manager
from api.utils.electricity_utils import power_generator_seq_num



@app.post("/power_generator")

def create_power_generator(request: AddPowerGeneratorRequestBody, db: Session = Depends(get_db)):
    try:
    #check if household has power_generator records
        request.seq_num = power_generator_seq_num(db, request.email)
            
        power_generator_Manager.createPowerGenerator(db=db, obj_in=request)

        # Construct and return the response
        return {"message": f"{request.email} power generator {request.seq_num} created"}
    
    except Exception as e:
        # Handle exceptions and rollback transactions if necessary
        raise HTTPException(status_code=400, detail=str(e))
    
@app.delete("/power_generator")

def delete_power_generator(request:DeletePowerGenerator, db: Session = Depends(get_db)):
    try:
        power_generator_Manager.deletePowerGenerator(db=db, obj_in=request)
        return {"message": f"{request.email} power generator {request.seq_num} deleted"}
    
    except Exception as e:
        # Handle exceptions and rollback transactions if necessary
        raise HTTPException(status_code=400, detail=str(e))