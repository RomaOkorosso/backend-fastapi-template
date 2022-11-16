import os
import json
from fastapi.security import HTTPBasic, OAuth2PasswordBearer


security = HTTPBasic()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")


def make_short_name(full_name: str):
    full_name = full_name.replace("\n", " ")
    return (
        full_name.split(" ")[0]
        + " "
        + full_name.split(" ")[1][0]
        + "."
        + full_name.split(" ")[2][0]
        + "."
    )


def group_by(items, key):
    res = {}
    for item in items:
        if key(item) not in res:
            res[key(item)] = []
        res[key(item)].append(item)
    return res


def get_json_from_file(file_path: str, encoding="utf-8"):
    if not os.path.exists(file_path):
        return None

    with open(file_path, encoding=encoding) as f:
        content = json.load(f)
        return content
