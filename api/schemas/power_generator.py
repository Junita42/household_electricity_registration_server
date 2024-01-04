from pydantic import BaseModel
from enum import Enum

class EnergySourceEnum(str, Enum):
    solar = "solar"
    wind_turbine = "wind-turbine"
    
    
class AddPowerGeneratorRequestBody(BaseModel):
    email: str
    seq_num: int
    battery_storage: int
    kilowatt_hours: int
    energy_source: EnergySourceEnum
    
class addPowerGeneratorResponse(BaseModel):
    email: str
    seq_num: int
    battery_storage: int
    kilowatt_hours: int
    energy_source: EnergySourceEnum
    
    
class DeletePowerGenerator(BaseModel):
    email: str
    seq_num: int
    