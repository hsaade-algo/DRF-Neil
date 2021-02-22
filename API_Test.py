import requests
import json


# POST Request to the Login Endpoint
url = 'http://127.0.0.1:8000/api/login/'

body = {
        'username': 'foo',
        'password': 'Password321'
}

response = requests.post(url, data=body)

# token = json.loads(response.text)['token']
token = response.json()["token"]
print("\nToken: ", token)


# GET Request to the Foo Endpoint
url = 'http://127.0.0.1:8000/api/foo/'

auth = 'token ' + token
headers = {
    'Content-Type': 'application/json',
    'Authorization': auth
}

response = requests.get(url, headers=headers)
print('\nGET Response: \n', response.text)


# POST to Insert Record
url = 'http://127.0.0.1:8000/api/foo/'
headers = {
    'Content-Type': 'application/json',
    'Authorization': auth
}

body = {
        "title": "A NEW post from the Python Requests lib",
        "content": "Lorem Ipsum",
        "author": 1
}
response = requests.post(url, json=body, headers=headers)
NewRecordID = response.json()['id']
print('\nNew Record Inserted >>', response.json())


# PATCH Request to update record
url = "http://127.0.0.1:8000/api/foo/" + str(NewRecordID) + '/'
print(url)
body = {
        "title": "UPDATED post from the Python Requests lib",
}
response = requests.patch(url, json=body, headers=headers)
print("\nRecord ID %s was updated with a new Status Text!" %NewRecordID)
print(response.json())
