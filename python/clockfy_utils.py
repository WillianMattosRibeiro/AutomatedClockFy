import requests
import json


def get_user(api_url, headers):
    r = requests.get(url=f"{api_url}/user", headers=headers)
    return json.loads(r.content)


def get_tags(api_url, headers, workspace_id, tag_name=None):
    params = {"page-size": 2000}

    if tag_name:
        params["name"] = tag_name

    r = requests.get(
        url=f"{api_url}/workspaces/{workspace_id}/tags",
        headers=headers,
        params=params)

    return json.loads(r.content)


def get_projects(api_url, headers, workspace_id, user_id, user_status=None):
    params = {"page-size": 5000,
              "users": [user_id]}

    if user_status:
        params["user-status"] = user_status

    r = requests.get(url=f"{api_url}/workspaces/{workspace_id}/projects",
                     headers=headers,
                     params=params
                     )
    return json.loads(r.content)


def set_time_entry(url, headers, workspace_id, date, hour, description, project_id, tags, debbug=None):
    import json

    time_entry_settings = {
        "start": f"{date}T{hour['start']}Z",
        "description": description,
        "projectId": project_id,
        "end": f"{date}T{hour['end']}Z",
        "tagIds": tags
    }

    data = json.dumps(time_entry_settings)
    r = requests.post(url=f"{url}/workspaces/{workspace_id}/time-entries", data=data, headers=headers)

    if debbug:
        print(r.status_code, r.content)
