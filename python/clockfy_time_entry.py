from utils.will_utils import get_json
from clockfy_utils import get_projects, get_tags, get_user, get_workspaces, set_time_entry
import os


def get_tags_list(base_url, headers, workspace):
    print("loading tags...")
    tags = get_tags(base_url, headers, workspace)
    tags_list = []
    for tag in tags:
        tags_list.append({"name": tag["name"], "id": tag["id"]})
    return tags_list


def get_workspace_id(base_url, headers):
    print("loading workspaces...")
    workspaces = get_workspaces(base_url, headers)
    workspace_id = workspaces[0]["id"]
    return workspace_id


def get_user_id(base_url, headers):
    print("loading users...")
    user = get_user(base_url, headers)
    user_id = user["id"]
    return user_id


def get_projects_list(base_url, headers, workspace, user_id):
    print("loading projects...")
    projects = get_projects(base_url, headers, workspace, user_id=user_id, user_status="ACTIVE")
    project_list = []
    for project in projects:
        project_list.append({"name": project["name"], "id": project["id"]})
    return project_list


class ClockfyTimeEntry:
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/")
        self.path_parameters = f"{self.root_dir}/json/parameters.json"
        self.parameters = get_json(self.path_parameters)
        self.credentials_file = get_json(f"{self.root_dir}/{self.parameters['CREDENTIALS_PATH']}")
        self.base_url = self.parameters["API_URL"]
        time_entry_path = self.parameters["TIME_ENTRY_BASE_PATH"]
        self.time_entry_path = time_entry_path.replace("{workspace}", self.credentials_file["workspace"])
        credentials = self.credentials_file["api_key"]

        self.headers = {'X-Api-Key': '{}'.format(credentials),
                        'Content-Type': 'application/json'}

        # self.workspace = self.credentials_file["workspace"]
        self.workspace = get_workspace_id(self.base_url, self.headers)

        self.hour = {"inicio": "09:00:00",
                     "fim": "13:00:00"}
        self.user_id = get_user_id(self.base_url, self.headers)
        self.projects_list = get_projects_list(self.base_url, self.headers, self.workspace, self.user_id)
        self.tags_list = get_tags_list(self.base_url, self.headers, self.workspace)

    def post_data_to_clockfy(self, args):

        debbug = False

        # TODO: encapsular metodo para adicionar fuso-horario nas horas inputadas como argumentos
        from datetime import datetime, timedelta
        start = (datetime.strptime(args["start_hour"], '%H:%M:%S') + timedelta(hours=3)).strftime("%H:%M:%S")
        end = (datetime.strptime(args["end_hour"], '%H:%M:%S') + timedelta(hours=3)).strftime("%H:%M:%S")

        set_time_entry(url=self.base_url,
                       headers=self.headers,
                       workspace_id=self.workspace,
                       date=args["date"],
                       hour={"start": start, "end": end},
                       description=args['description'],
                       project_id=args["project"],
                       tags=args["tags"],
                       debbug=debbug)
