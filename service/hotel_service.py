import sys 
import os
import requests
import uuid
from fastapi import HTTPException

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# from db.db_init import DB_mysql

hotel_list_url = "https://hotels4.p.rapidapi.com/properties/v2/list"
region_list_url = "https://hotels4.p.rapidapi.com/locations/v3/search"

def request_hotel_list(context):
    try:
        # OpenAI API를 통한 chatCompletion 요청
        
        payload = {
            "currency": "USD",
            "eapid": 1,
            "locale": "en_US",
            "siteId": 300000001,
            "destination": {"regionId": context.regionId},
            "checkInDate": {
                "day": int(context.checkInDate.split('/')[0]),
                "month": int(context.checkInDate.split('/')[1]),
                "year": int(context.checkInDate.split('/')[2])
            },
            "checkOutDate": {
                "day": int(context.checkOutDate.split('/')[0]),
                "month": int(context.checkOutDate.split('/')[1]),
                "year": int(context.checkOutDate.split('/')[2])
            },
            "rooms": [
                {
                    "adults": context.roomAdultCount,
                    "children": [{"age": age} for age in context.roomChildren]
                }
            ],
            "resultsStartingIndex": 0,
            "resultsSize": 200,
            "sort": "PRICE_LOW_TO_HIGH",
            "filters": {
                "price": {
                    "max": context.priceMax,
                    "min": context.priceMin
                }
            }
        }

        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "ccaeb0a33dmshb230c8e90ba62eep1ff9afjsn7c6640a7ce77",
            "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
        }

        response = requests.post(hotel_list_url, json=payload, headers=headers)
        data = response.json()['data']['propertySearch']['properties']
        print(data)
        # db_instance = DB_mysql()
        search_id = uuid.uuid4
        
        # for row in data:
        #     db_instance.insert_hotel_row(hotel_data = row, search_id=search_id)
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def request_region_list(context):
    try:
        payload = {"q":context.region_name,"locale":"en_US","langid":"1033","siteid":"300000001",}

        headers = {
            "X-RapidAPI-Key": "ccaeb0a33dmshb230c8e90ba62eep1ff9afjsn7c6640a7ce77",
            "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
        }
        response = requests.post(hotel_list_url, params=payload, headers=headers)
        # API 응답에서 assistant의 답변만 추출하여 반환
        data = response.json()['data']['propertySearch']['properties']

        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))