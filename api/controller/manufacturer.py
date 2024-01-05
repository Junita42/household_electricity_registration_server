from api.schemas.manufacturer import GetMultiManufacturerResponse
from main import app


# @app.get("/manufacturers", response_model=GetMultiManufacturerResponse)
# def get_all_manufacturers():
#     """Get all manufacturers."""
#     # manufacturers = Manufacturer.query.all()
 
#     manu_list: GetMultiManufacturerResponse = GetMultiManufacturerResponse(manufacturers=manufacturers)
#     return manu_list

