import requests
import os
from datetime import datetime

TOKEN = os.environ.get("TOKEN")
USER_NAME = os.environ.get("USER_NAME")
CYCLING_GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# CREATE USER:
# response = requests.post(url=pixela_endpoint, json=user_params)

# create graph:
# graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
# graph_config = {
#     "id": CYCLING_GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
#
# create_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# create_graph.raise_for_status()

# CREATE PIXEL:
# post_pixel = f"{pixela_endpoint}/{USER_NAME}/graphs/{CYCLING_GRAPH_ID}"
# today = datetime.now()
# pixel_config_post = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "10.4"
# }
#
# pixel_post_response = requests.post(url=post_pixel, json=pixel_config_post, headers=headers)
# pixel_post_response.raise_for_status()

# UPDATE PIXEL
# date = "20231207"
# update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{CYCLING_GRAPH_ID}/{date}"
# pixel_config_put = {
#     "quantity": "4.2"
# }
#
# update_pixel = requests.put(url=update_pixel_endpoint, json=pixel_config_put, headers=headers)
# update_pixel.raise_for_status()


# DELETE PIXEL
# delete_date = "20231207"
# delete_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{CYCLING_GRAPH_ID}/{delete_date}"
# delete_pixel = requests.delete(url=delete_pixel_endpoint, headers=headers)
# delete_pixel.raise_for_status()