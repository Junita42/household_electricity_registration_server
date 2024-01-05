
from typing import List
from pydantic import BaseModel
       
from enum import Enum
import os


# Path to your TSV file
tsv_file_path = './data/Demo_Data/Manufacturer.tsv'


def read_manufacturers_from_tsv(file_path):
    with open(file_path, 'r') as file:
        # Assuming each line in the file is a unique manufacturer name
        return {line.strip().upper().replace(" ", "_"): line.strip() for line in file}

def create_manufacture_enum(tsv_file_path):
    if os.path.exists(tsv_file_path):
        manufacturers = read_manufacturers_from_tsv(tsv_file_path)
        # Dynamically create an Enum using the functional API
        ManufactureEnum = Enum('ManufactureEnum', manufacturers)
        return ManufactureEnum
    else:
        raise FileNotFoundError(f"The file {tsv_file_path} does not exist.")

# Example usage

ManufactureEnum = create_manufacture_enum(tsv_file_path)

   
class GetMultiManufacturerResponse(BaseModel):
    manufacturers: List[ManufactureEnum] 