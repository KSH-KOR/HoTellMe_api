import sys 
import os
from fastapi import APIRouter

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from request.post_hotel_list import RequestHotelList
from request.post_region_list import RequestRegionList
from service.hotel_service import request_hotel_list, request_region_list
from response.post_hotel_list import ResponseHotelList, ResponseRegionList

hotel_router = APIRouter()

@hotel_router.post("/request/hotel-list")
async def request_chat_summary(request: RequestHotelList):
    success = request_hotel_list(context=request)
    return ResponseHotelList(success = success)

@hotel_router.post("/request/region-list")
async def request_chat_response(request: RequestRegionList):
    success = request_region_list(context=request)
    return ResponseRegionList(success = success)
