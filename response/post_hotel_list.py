from pydantic import BaseModel

class ResponseHotelList(BaseModel):
    success: bool

class ResponseRegionList(BaseModel):
    success: bool