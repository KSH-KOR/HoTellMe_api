import requests
from datetime import datetime
from pydantic import BaseModel
from typing import List


class RequestHotelList(BaseModel):
    regionId: str
    checkInDate: str  # dd/mm/yyyy
    checkOutDate: str  # dd/mm/yyyy
    roomAdultCount: int
    roomChildren: List[int]
    priceMax: int
    priceMin: int

# Define your API endpoint URL
url = "http://101.101.219.108:8001/request/hotel-list"

# Create an instance of RequestHotelList with example data
request_data = RequestHotelList(
    regionId="8077",
    checkInDate="01/08/2023",
    checkOutDate="10/08/2023",
    roomAdultCount=2,
    roomChildren=[5, 7],
    priceMax=1000,
    priceMin=100
)

# Send the POST request
response = requests.post(url, json=request_data.dict())

# Check the response
if response.status_code == 200:
    print("Request successful:")
    print(response.json())
else:
    print("Request failed with status code:", response.status_code)
    print(response.text)
