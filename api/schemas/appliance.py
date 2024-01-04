from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, List
from api.schemas.manufacturer import ManufactureEnum
# 1. add appliance

# Define validations for the fields having limited choices 


class applianceEnum(str, Enum):
    air_handler = "air handler"
    water_heater = "water heater"


class HeaterEnergySourceEnum(str, Enum):
    electric = "electric"
    gas = "gas"
    thermosolar = "thermosolar"
class energySourceEnum(str, Enum):
    electric = "electric"
    heat_pump = "heat pump"
    fuel_oil = "fuel oil"

# Define the request body    

class getApplianceByEmailRequestBody(BaseModel):
    email:str

class AddApplianceRequestBody(BaseModel):
    email: str
    seq_num: Optional[int]
    manufacturer: ManufactureEnum
    electricity_model: Optional[str] 
    BTU: int
    appliance_type: applianceEnum
    RPM: Optional[int] = None
    EER: Optional[int] = None
    energy_source: Optional[HeaterEnergySourceEnum] = None
    SEER: Optional[float] = None
    HSPF: Optional[float] = None
    tank_size: Optional[float] = None
    current_temp: Optional[int] = None
         
        
         
# Define the response body
class ApplianceResponse(BaseModel):
    manufacture: ManufactureEnum
    seq_num: int
    electricity_model: Optional[str] 
    appliance_type: applianceEnum
    

# define the delete appliance request body
class DeleteAppliance(BaseModel):
    email: str
    seq_num: int
    appliance_type: applianceEnum
    
  


