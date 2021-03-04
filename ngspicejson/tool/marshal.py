import json


def global_marshal(type, contents, real=""):
    return json.dumps({"type": type, "contents": contents, "real": real})
