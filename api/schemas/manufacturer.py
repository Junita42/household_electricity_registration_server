
from typing import List
from pydantic import BaseModel
from enum import Enum


class Manufacturer(BaseModel):
    manufacturer_name: str

# Read manufacturers from the TSV file
def read_manufacturers_from_tsv(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Path to your TSV file
tsv_file_path = './data/Demo_Data/Manufacturer.tsv'

# Create the Enum class

class ManufactureEnum(str, Enum):
    for name in read_manufacturers_from_tsv(tsv_file_path):
        exec(name.upper().replace(" ", "_") + " = '" + name + "'")     
class GetMultiManufacturerResponse(BaseModel):
    manufacturers: List[ManufactureEnum] 


