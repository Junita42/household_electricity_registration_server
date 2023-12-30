from pydantic import BaseModel, str
from enum import Enum

class EnergySourceEnum(str, Enum):
    solar = "solar"
    wind_turbine = "wind-turbine"
    
    
class AddPowerGenerationRequestBody(BaseModel):
    email: str
    battery_storage: int
    kilowatt_hour: int
    energy_source: EnergySourceEnum
    
class addPowerGenerationResponse(BaseModel):
    seq_num: int
    battery_storage: int
    kilowatt_hour: int
    energy_source: EnergySourceEnum
    
    
class DeletePowerGeneration(BaseModel):
    email: str
    seq_num: int
    