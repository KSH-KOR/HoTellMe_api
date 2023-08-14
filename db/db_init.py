import pyodbc

class DBInfo():
    server = "bizmedudev.bizflow.com:1433"
    user = "hgu13_user"
    passwd = "hgu13"
    db_name = "hgu13"
    charset = "utf8"
    driver = "ODBC Driver 17 for SQL Server"

    @staticmethod
    def get_connection_string():
        return f"DRIVER={DBInfo.driver};SERVER={DBInfo.server};DATABASE={DBInfo.db_name};UID={DBInfo.user};PWD={DBInfo.passwd}"

class DB_mysql():
    session = None
    def __init__(self):
        self.session = self.init_db()
        self.cur = self.session.cursor()

    def __del__(self): 
        self.cur.close()
        self.session.close()

    def init_db(self):
        return pyodbc.connect(DBInfo.get_connection_string())
    
    def get_cursor(self):
        try:
            self.session.ping(reconnect=True, attempts=3, delay=5)
        except :
            self.session = self.init_db()
            self.cur = self.session.cursor()
    
    def send_insert_query(self, sql):
        self.get_cursor()
        self.cur.execute(sql)
        self.session.commit()

    def send_select_query(self, sql):     
        self.get_cursor()
        self.cur.execute(sql)
        return list(self.cur.fetchall())

    def insert_hotel_row(self, hotel_data):
        availability = 1 if hotel_data['availability']['available'] else 0
        distance_from_messaging = hotel_data['destinationInfo']['distanceFromMessaging']
        id = hotel_data['id']
        name = hotel_data['name']
        latitude = hotel_data['mapMarker']['latLong']['latitude']
        longitude = hotel_data['mapMarker']['latLong']['longitude']
        price_amount = hotel_data['price']['lead']['amount']
        price_unit_symbol = hotel_data['price']['lead']['currencyInfo']['symbol']
        property_image_url = hotel_data['propertyImage']['image']['url']
        review_score = hotel_data['reviews']['score']
        review_count = hotel_data['reviews']['total']

        escaped_name = name.replace("'", "''")
        # Insert data into the table
        insert_query = f"""
INSERT INTO HotelData (Availability, DistanceFromMessaging, Name, Id, Latitude, Longitude, PriceAmount, PriceUnitSymbol, PropertyImageUrl, ReviewScore, ReviewCount)
VALUES ({availability}, '{distance_from_messaging}', '{escaped_name}', '{id}', {latitude}, {longitude}, {price_amount}, '{price_unit_symbol}', '{property_image_url}', {review_score}, {review_count})
        """
        
        self.send_insert_query(insert_query)

