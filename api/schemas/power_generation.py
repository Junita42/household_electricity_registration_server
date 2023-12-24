from pydantic import BaseModel


class AddPowerGenerationRequestBody(BaseModel):
    email: str
    seq_num: int
    battery_storage: int
    kilowatt_hour: int
    energy_source: str
    
class addPowerGenerationResponse(BaseModel):
    seq_num: int
    battery_storage: int
    kilowatt_hour: int
    energy_source: str
    
    
class DeletePowerGeneration(BaseModel):
    email: str
    seq_num: int
    