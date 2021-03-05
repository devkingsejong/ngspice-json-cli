import json


def global_marshal(type, contents, real=""):
    return {"type": type, "contents": contents, "real": real}
