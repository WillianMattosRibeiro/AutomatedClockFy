def get_json(path):
    import json
    f = open(path)
    return json.load(f)
