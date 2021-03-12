KEY_TITLE = "key"
VALUE_TITLE = "values"


def global_marshal(type, contents, real=""):
    return {"type": type, "contents": contents, "real": real}


def simple_keyvalues_marshal(key, value):
    if type(value) != list:
        value = [value]

    return {KEY_TITLE: key, VALUE_TITLE: value}


def dynamic_keyvalues_marshal(key_title, key, value):
    if type(value) != list:
        value = [value]

    return {key_title: key, VALUE_TITLE: value}
