from .marshal import global_marshal


def global_exception(title, description):
    print(global_marshal("EXCEPTION", {"title": title, "description": description}))
