import pymongo

url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(url)

db = client['spendo_db']

# Testing the connection: 
try:
    server_info = client.server_info()
    print("Connection Successful")
except Exception as exception:
    print("Connection Failed")