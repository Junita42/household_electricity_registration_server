
from pydantic import BaseModel

# 1. add appliance
class AddApplianceRequestBody(BaseModel):
     email: str
     manufacture: str
     seq_num: int
     model_name: str
     BTU: int
     appliance_type: str
     if appliance_type == 'air_handler':
         air_handler_type: str
         RPM: int
         if "Air_conditioner" in air_handler_type:
             EER: int
         if "heater" in air_handler_type:
             energy_source: str
         if "heat_pump" in air_handler_type:
             SEER: float
             HSPF: float
     else:
         tank_size: float
         energy_source: str
         current_temp: int
         

class addApplianceResponse(BaseModel):
    manufacture: str
    seq_num: int
    model_name: str
    appliance_type: str
    

#2. delete appliance
class DeleteAppliance(BaseModel):
    email: str
    seq_num: int
    
  


