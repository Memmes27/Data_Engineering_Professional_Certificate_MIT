from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Connect to the employee database
db = client['employee']

# Get the employees collection
collection = db['employees']

# Create filter for Rose
filter = {"LastName": "Rose"}

# Delete one record
collection.delete_one(filter)

# Print all remaining employees
for employee in collection.find():
    print(employee)