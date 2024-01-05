
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List


    
class AddThermalHeatingRequestBody(BaseModel):
    email: str
    heating: bool
    setting: Optional[int]

class AddThermalCoolingRequestBody(BaseModel):
    email: str
    cooling: bool
    setting: Optional[int]


# class ThermalRequestBody(BaseModel):
#     email: str
#     heating: bool
#     cooling: bool
#     heat_setting: Optional[int]
#     cool_setting: Optional[int]


class DeleteThermal(BaseModel):
    email: str