from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['flight_status_db']
flight_logs = db['flight_logs']
