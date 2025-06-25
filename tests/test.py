import requests

BASE_URL = "http://34.203.68.1:8080" 

# Login
login_data = {
    "User_mail": "allan",
    "password": "1234"
}

login_response = requests.post("http://52.203.72.116:8080/login", json=login_data)
if login_response.status_code != 200:
    print("Error en login:", login_response.status_code, login_response.json())
    exit()

token = login_response.json()["token"]
print("Token:", token)

# User to unfollow
data_unfollow = {
    "id_following": 4  # ID to unfollow
}

headers = {
    "Authorization": f"Bearer {token}"
}

# Unfollow
unfollow_response = requests.post(f"{BASE_URL}/unfollow", json=data_unfollow, headers=headers)

print("\nUnfollow response:")
print(unfollow_response.status_code, unfollow_response.json())

