import os
import requests
from datetime import datetime

#Creating Username and Token
PIXEL_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = os.getenv("TOKEN")
USERNAME = "uknowme"

pixel_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(PIXEL_ENDPOINT , json=pixel_params)
# print(response.text)

#Creating a Graph
graph_endpoint = f"{PIXEL_ENDPOINT}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "id": "coding-graph",
    "name": "Coding Tracker",
    "unit": "hours",
    "type": "float",
    "color": "shibafu"  # Green color
}

# graph_response = requests.post(url=graph_endpoint , json=graph_params , headers=headers)
# print(graph_response.text)

#Creating a Pixel
today = datetime.now().strftime('%Y%m%d')

creation_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_params['id']}"


creation_params = {
    "date" : today,
    "quantity" : "9.5",
}

# pixel_create = requests.post(url=creation_endpoint , json=creation_params , headers=headers)
# print(pixel_create.text)


#Updating a Pixel
pixel_update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_params['id']}/{today}"

update_data = { "quantity" : "7.5"}

# pixel_update_response = requests.put(url=pixel_update_endpoint, json=update_data, headers=headers)
# print(pixel_update_response.text)

#Deleting a Pixel
today = datetime(year=2025 , month=10, day=21)

delete_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_params['id']}/{today}"

pixel_delete = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(pixel_delete.text)





