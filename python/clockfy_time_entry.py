#LANCADOR DE HORAS NO CLOCKFY
from utils.will_utils import get_json
from datetime import datetime
import requests
import json

path_parameters = ".\json\parameters.json"
parameters = get_json(path_parameters)

path_credentials = ".\credentials\credentials.json"
credentials_file = get_json(path_credentials)

base_url = parameters["api_url"]
time_entry_path = parameters["time_entry_base_path"]
time_entry_path = time_entry_path.replace("{workspace}", credentials_file["workspace"])
credentials = credentials_file["api_key"]

# print(base_url)
# print(credentials)
# print(time_entry_path)

workspace = credentials_file["workspace"]

# TIME ENTRY CONFIG

billable = "true"
description = "teste"

####################



url = '{}{}'.format(base_url, time_entry_path)
#print(url)
headers = {'X-Api-Key': '{}'.format(credentials),
            'Content-Type': 'application/json'}

date_now = datetime.now().strftime("%Y-%m-%d")


from clockfy_utils import get_user, get_tags, get_projects

teste = "https://api.clockify.me/api/v1"
print("capturando usuarios: ")
user = get_user(teste, headers)
json_user = json.loads(user)
print("id = ", json_user["id"], "\nname = ", json_user["name"])

print("capturando tags: ")
api_tags = get_tags(teste, headers, workspace)
json_tags = json.loads(api_tags)

tags = []
for tag in json_tags:
    if tag["name"] == "Reunião":
        print(tag["name"], " - id: ", tag["id"])
        tags.append(tag["id"])

api_projects = get_projects(teste, headers, workspace, user_id=json_user["id"], user_status="ACTIVE")
json_projects = json.loads(api_projects)
#print(json_projects)

project_id = None
for project in json_projects:
    if project["name"] == "Desenvolvimento de Conteúdo":
        project_id = project['id']
        print(f"Projeto: {project['name']} - {project['id']}\n\n#################################")
    else:
        print("PROJETO NAO ENCONTRADO!")

first_time = {
  "start": f"{date_now}T12:00:00.000Z",
  "description": description,
  "projectId": project_id,
  "end": f"{date_now}T15:00:00.000Z",
  "tagIds": tags
}

# second_time = {
#   "start": "{}T16:00:00.000Z".format(date_now),
#   "billable": "true",
#   "description": "BRF e Gestao Squad",
#   "projectId": "5ef21ac043162e08f73ac890",
#   "end": "{}T21:00:00.000Z".format(date_now),
#   "tagIds": [
#      "5e72352dcb758f10a10e61af",
#      "5e723533d5d30e3d6f0a45f5",
#      "5e8f554c3b138c4dc4465c72"
#    ]
# }

data=json.dumps(first_time)
r = requests.post(url, data=json.dumps(first_time), headers=headers)
print(r.status_code)
print(r.content)

# r = requests.post(url, data=json.dumps(second_time), headers=headers)
# print(r.content)
