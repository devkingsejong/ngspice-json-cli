from .marshal import global_marshal
import json


class GlobalException(Exception):
    def __init__(self, title="GlobalException", description="Raised Global Exception."):
        self.title = title
        self.description = description

    def __str__(self):
        return json.dumps(global_marshal("EXCEPTION", {"title": self.title, "description": self.description}))
