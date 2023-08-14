import pyodbc

# Database information
db_url = "bizmedudev.bizflow.com:1433"
db_name = "hgu13"
db_user = "hgu13_user"
db_password = "hgu13"

# Create a connection to the database
connection_string = f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={db_url};DATABASE={db_name};UID={db_user};PWD={db_password}"
connection = pyodbc.connect(connection_string)

# Create a cursor
cursor = connection.cursor()

# Create a table if it doesn't exist
cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'HotelData')
    BEGIN
        CREATE TABLE HotelData (
            Availability BIT,
            DistanceFromMessaging NVARCHAR(100),
            Name NVARCHAR(200),
            Id NVARCHAR(50) PRIMARY KEY,
            Latitude FLOAT,
            Longitude FLOAT,
            PriceAmount FLOAT,
            PriceUnitSymbol NVARCHAR(10),
            PropertyImageUrl NVARCHAR(200),
            ReviewScore FLOAT,
            ReviewCount INT
        )
    END
""")

connection.close()

print("Data has been saved to the database.")
