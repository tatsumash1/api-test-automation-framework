import requests

#GET /api/users/2
"""
HTTP status == 200

data.id == 2

data.email существует

data.first_name существует

data.last_name существует
"""
def test_response_from_server():
    response = requests.get("https://reqres.in/api")
    print(response)

test_response_from_server()