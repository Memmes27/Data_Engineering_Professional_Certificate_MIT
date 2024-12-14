from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Connect to the employee database
db = client['employee']

# Get the employees collection
collection = db['employees']

# Create filter for Smith employees
filter = {"LastName": "Smith"}

# Define the new department value
newvalues = { "$set": { "Department": "Computer Science" } }

# Update multiple records
collection.update_many(filter, newvalues)

# Print all employees to verify the update
for employee in collection.find():
    print(employee)