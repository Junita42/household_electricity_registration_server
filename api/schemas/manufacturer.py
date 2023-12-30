
from typing import List
from pydantic import BaseModel
from enum import Enum

# Create the Enum class
  
        
from enum import Enum
import os


# Path to your TSV file
tsv_file_path = './data/Demo_Data/Manufacturer.tsv'

def read_manufacturers_from_tsv(file_path):
    with open(file_path, 'r') as file:
        # Assuming each line in the file is a unique manufacturer name
        return {line.strip().upper().replace(" ", "_"): line.strip() for line in file}

tsv_file_path = 'path_to_your_tsv_file.tsv'

class ManufactureEnum(str, Enum):
    if os.path.exists(tsv_file_path):
        manufacturers = read_manufacturers_from_tsv(tsv_file_path)
        # Dynamically adding Enum members
        locals().update(manufacturers)

   
class GetMultiManufacturerResponse(BaseModel):
    manufacturers: List[ManufactureEnum] 


