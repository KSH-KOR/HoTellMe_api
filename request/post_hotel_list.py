from pydantic import BaseModel
from typing import List


class RequestHotelList(BaseModel):
    regionId: str
    checkInDate: str #dd/mm/yyyy
    checkOutDate: str #dd/mm/yyyy
    roomAdultCount: int
    roomChildren: List[int]
    priceMax: int
    priceMin: int