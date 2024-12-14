# firebase - backend as a service, BaaS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://assignment-module12-d699b-default-rtdb.firebaseio.com/'
})

# save data
ref = db.reference('py/')
entries_ref = ref.child('entries')
entries_ref.set({
    'entry1': {
        'name': 'First Entry',
        'description': 'This is my first Firebase entry',
        'date': '2024-12-14'
    },
    'entry2': {
        'name': 'Second Entry',
        'description': 'This is my second Firebase entry',
        'date': '2024-12-14'
    }
})

# update data with extra field
update_ref = entries_ref.child('entry2')
update_ref.update({
    'extra_field': 'This is an additional field for the second entry'
})

# read and print data
print(ref.get())