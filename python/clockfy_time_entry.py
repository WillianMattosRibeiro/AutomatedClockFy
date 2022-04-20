from utils.will_utils import get_json
from clockfy_utils import get_tags, get_projects, get_user, set_time_entry


def get_tags_name(base_url, headers, workspace):
    # - CARREGAR INFORMAÇÔES DE TAGS
    print("capturando tags: ")
    tag_name = "Reunião"
    tags = get_tags(base_url, headers, workspace, tag_name)
    tags_list = []
    for tag in tags:
        if tag["name"] == tag_name:
            tags_list.append(tag["id"])
    return tags_list


def get_user_id(base_url, headers):
    print("capturando usuarios: ")
    user = get_user(base_url, headers)
    user_id = user["id"]
    return user_id


def get_project_id(base_url, headers, workspace, user_id):
    # - CARREGAR INFORMAÇÔES DE PROJETO
    print("capturando projetos: ")
    projects = get_projects(base_url, headers, workspace, user_id=user_id, user_status="ACTIVE")
    project_id = None
    for project in projects:
        if project["name"] == "Desenvolvimento de Conteúdo":
            project_id = project['id']
    return project_id


class ClockfyTimeEntry:
    def __init__(self):
        self.path_parameters = "./json/parameters.json"
        self.parameters = get_json(self.path_parameters)

        self.credentials_file = get_json(self.parameters["CREDENTIALS_PATH"])

        self.base_url = self.parameters["API_URL"]

        time_entry_path = self.parameters["TIME_ENTRY_BASE_PATH"]
        self.time_entry_path = time_entry_path.replace("{workspace}", self.credentials_file["workspace"])

        credentials = self.credentials_file["api_key"]

        self.workspace = self.credentials_file["workspace"]

        self.headers = {'X-Api-Key': '{}'.format(credentials),
                        'Content-Type': 'application/json'}

        self.hour = {"inicio": "hora_inicio",
                     "fim": "hora_fim"}

        self.user_id = get_user_id(self.base_url, self.headers)

    def post_data_to_clockfy(self, args):

        debbug = True

        print(self.base_url)
        print(self.headers)
        print(self.workspace)
        print(args["data"])
        print({"start": args["hora_inicio"], "end": args["hora_fim"]})
        print(args['description'])

        project_id = ""
        for project in get_projects(self.base_url, self.headers, self.workspace, self.user_id):
            if project["name"] == args["projeto"]:
                print(project['id'])
                project_id = project['id']

        tag_list = []
        for tag in get_tags(self.base_url, self.headers, self.workspace, args['tags']):
            if tag["name"] == args["tags"]:
                print(tag['id'])
                tag_list.append(tag['id'])

        set_time_entry(url=self.base_url,
                       headers=self.headers,
                       workspace_id=self.workspace,
                       date=args["data"],
                       hour={"start": args["hora_inicio"], "end": args["hora_fim"]},
                       description=args['description'],
                       project_id=project_id,
                       tags=tag_list,
                       debbug=debbug)
