import json

# Open the JSON file for reading
with open('data.json', 'r') as file:
    data = json.load(file)

query_list = []

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
    # Insert data into the table
    insert_query = f"""
INSERT INTO HotelData (Availability, DistanceFromMessaging, Name, Id, Latitude, Longitude, PriceAmount, PriceUnitSymbol, PropertyImageUrl, ReviewScore, ReviewCount)
VALUES ({availability}, '{distance_from_messaging}', '{escaped_name}', '{id}', {latitude}, {longitude}, {price_amount}, '{price_unit_symbol}', '{property_image_url}', {review_score}, {review_count})
    """
    
    query_list.append(insert_query)

# Write the query_list to a SQL file
with open('insert_queries.sql', 'w') as sql_file:
    for query in query_list:
        sql_file.write(query + '\n')