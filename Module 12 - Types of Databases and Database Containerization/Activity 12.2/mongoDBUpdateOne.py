from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Connect to the employee database
db = client['employee']

# Get the employees collection
collection = db['employees']

# Create filter for Helen Rose
filter = {"LastName": "Rose"}

# Define the new age value
newvalues = { "$set": { "Age": 32 } }

# Update the record
collection.update_one(filter, newvalues)

# Show the updated record
updated_employee = collection.find_one({"LastName": "Rose"})
print(updated_employee)