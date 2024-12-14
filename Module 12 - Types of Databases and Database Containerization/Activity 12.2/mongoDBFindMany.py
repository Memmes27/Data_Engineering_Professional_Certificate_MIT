from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Connect to the employee database
db = client['employee']

# Get the employees collection
collection = db['employees']

# Find all employees with LastName = "Smith"
employeeCursor = collection.find({"LastName": "Smith"})

# Loop through and print all matching employees
for employee in employeeCursor:
    print(employee)