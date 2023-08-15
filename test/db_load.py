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

# text = json.dumps(data,sort_keys=True, indent=4)

# f = open("data.json", "wt")
# f.write(text)
# print(data)

