from enum import Enum
from pydantic import BaseModel, str
from typing import Optional, List
from api.schemas.manufacturer import ManufactureEnum
# 1. add appliance

# Define validations for the fields having limited choices 


class applianceEnum(str, Enum):
    air_handler = "air handler"
    water_heater = "water heater"

class airHandlerEnum(str, Enum):
    Air_conditioner = "Air conditioner"
    Heat_pump = "Heat pump"
    Heater = "Heater"

class HeaterEnergySourceEnum(str, Enum):
    electric = "electric"
    gas = "gas"
    thermosolar = "thermosolar"
class energySourceEnum(str, Enum):
    electric = "electric"
    heat_pump = "heat pump"
    fuel_oil = "fuel oil"

# Define the request body    
class AddApplianceRequestBody(BaseModel):
     email: str
     manufacture: ManufactureEnum
     model_name: Optional[str]
     BTU: int
     appliance_type: applianceEnum
     if appliance_type == 'air_handler':
         air_handler_type: airHandlerEnum
         RPM: int
         if "Air_conditioner" in air_handler_type:
             EER: int
         if "heater" in air_handler_type:
             energy_source: HeaterEnergySourceEnum
         if "heat_pump" in air_handler_type:
             SEER: float
             HSPF: float
     else:
         tank_size: float
         energy_source: energySourceEnum
         current_temp: int
         
# Define the response body
class ApplianceResponse(BaseModel):
    manufacture: ManufactureEnum
    seq_num: int
    model_name: Optional[str] 
    appliance_type: applianceEnum
    

# define the delete appliance request body
class DeleteAppliance(BaseModel):
    email: str
    seq_num: int
    
  


