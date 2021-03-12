from .marshal import global_marshal
import json


def global_exception(title, description):
    print(json.dumps(global_marshal("EXCEPTION", {"title": title, "description": description})))
