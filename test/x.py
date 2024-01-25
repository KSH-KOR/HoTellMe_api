import requests
import json

url = "https://hotels4.p.rapidapi.com/properties/v2/list"

payload = {
	"currency": "USD",
	"eapid": 1,
	"locale": "en_US",
	"siteId": 300000001,
	"destination": { "regionId": "8077" },
	"checkInDate": {
		"day": 10,
		"month": 10,
		"year": 2022
	},
	"checkOutDate": {
		"day": 15,
		"month": 10,
		"year": 2022
	},
	"rooms": [
		{
			"adults": 2,
			"children": [{ "age": 5 }, { "age": 7 }]
		}
	],
	"resultsStartingIndex": 0,
	"resultsSize": 200,
	"sort": "PRICE_LOW_TO_HIGH",
	"filters": { "price": {
			"max": 150,
			"min": 100
		} }
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "ccaeb0a33dmshb230c8e90ba62eep1ff9afjsn7c6640a7ce77",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)
data = response.json()['data']['propertySearch']['properties']

processed_data_list = []

# Insert data into the table
for item in data:
    availability = 1 if item['availability']['available'] else 0
    distance_from_messaging = item['destinationInfo']['distanceFromMessaging']
    id = item['id']
    name = item['name']
    latitude = item['mapMarker']['latLong']['latitude']
    longitude = item['mapMarker']['latLong']['longitude']
    price_amount = item['price']['lead']['amount']
    price_unit_symbol = item['price']['lead']['currencyInfo']['symbol']
    property_image_url = item['propertyImage']['image']['url']
    review_score = item['reviews']['score']
    review_count = item['reviews']['total']

    escaped_name = name.replace("'", "''")

    processed_data_list.append(
        {
            'Availability' : 1 if item['availability']['available'] else 0,
            'DistanceFromMessaging' : item['destinationInfo']['distanceFromMessaging'],
            'Id' : item['id'],
            'Name' : item['name'].replace("'", "''"),
            'Latitude' : item['mapMarker']['latLong']['latitude'],
            'Longitude' : item['mapMarker']['latLong']['longitude'],
            'PriceAmount' : item['price']['lead']['amount'],
            'priceUnitSymbol' : item['price']['lead']['currencyInfo']['symbol'],
            'propertyImageUrl' : item['propertyImage']['image']['url'],
            'reviewScore' : item['reviews']['score'],
            'reviewCount' : item['reviews']['total'],
        }
    )