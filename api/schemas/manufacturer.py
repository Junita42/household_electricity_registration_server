# 1. get all manufactures
from typing import List
from pydantic import BaseModel


class Manufacturer(BaseModel):
    manufacturer_name: str


class GetMultiManufacturerResponse(BaseModel):
    manufacturers: List[Manufacturer] = []



