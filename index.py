import requests
import os

# hero: spiderman

token = os.getenv('vercel_token')

prj_id_hello_world = "prj_7aSQJteZKfYCOv1c1JngW2BKavvh"
env_id_sec = "AjvNmTsb2pqAOf91"
update_env = f"https://api.vercel.com/v9/projects/{prj_id_hello_world}/env/{env_id_sec}"

headers = {
    "Authorization": f"Bearer {token}"
}

params = {
    # "key": "sec",
    # "comment":"asdf",
    # "customEnvironmentIds":[],
    # "comment": "good for all",
    # "target": ["development","preview","production"],
    # "type": "encrypted",
    "value": "iron man"
}

response = requests.patch(update_env, headers=headers, json=params)
