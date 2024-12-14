from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Connect to (or create) the EmployeeDB database
db = client['employee']

# Get the employees collection
collection = db['employees']

# Create the employee collection data
employeeCollection = [
    {"FirstName":"John", "LastName":"Smith", "Age":25},
    {"FirstName":"Peter", "LastName":"Smith", "Age":26},
    {"FirstName":"Gabriel", "LastName":"Smith", "Age":28},
    {"FirstName":"Penny", "LastName":"Lane", "Age":22},
    {"FirstName":"Eleanor", "LastName":"Rigby", "Age":23},
    {"FirstName":"Helen", "LastName":"Rose", "Age":23}
]

# Insert the collection
result = collection.insert_many(employeeCollection)

# Verify database creation
if "employee" in client.list_database_names():
    print("Employee database created!")

# Print the inserted IDs
print(result.inserted_ids)