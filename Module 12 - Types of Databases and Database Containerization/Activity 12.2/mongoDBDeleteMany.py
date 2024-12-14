from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Connect to the employee database
db = client['employee']

# Get the employees collection
collection = db['employees']

# Create filter for Smith employees
filter = {"LastName": "Smith"}

# Delete multiple records
collection.delete_many(filter)

# Print remaining employees
for employee in collection.find():
    print(employee)