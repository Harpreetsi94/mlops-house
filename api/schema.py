from pydantic import BaseModel

class HouseRequest(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int