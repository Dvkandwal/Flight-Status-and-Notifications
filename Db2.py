import psycopg2

conn = psycopg2.connect(
    dbname="flight_status_db",
    user="yourusername",
    password="yourpassword",
    host="localhost"
)

cursor = conn.cursor()
