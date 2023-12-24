from api.schemas.manufacturer import GetMultiManufacturerResponse
from api.server import app


@app.get("/manufacturers", response_model=GetMultiManufacturerResponse)
def get_all_manufacturers():
    """Get all manufacturers."""
    # manufacturers = Manufacturer.query.all()
    manufacturers = [
        {"manufacturer_name": "manufacturer1"},
        {"manufacturer_name": "manufacturer2"},
    ]
    manu_list: GetMultiManufacturerResponse = GetMultiManufacturerResponse(manufacturers=manufacturers)
    return manu_list

