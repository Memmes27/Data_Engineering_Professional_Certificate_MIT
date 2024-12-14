from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Connect to the employee database
db = client['employee']

# Get the employees collection
collection = db['employees']

# Find one employee with LastName = "Rigby"
employee = collection.find_one({"LastName": "Rigby"})

# Print the employee record
print(employee)