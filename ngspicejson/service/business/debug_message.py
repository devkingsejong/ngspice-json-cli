from ..tool.marshal import global_marshal, simple_keyvalues_marshal


def make_debug_message(tag, time, real_command, real=False):
    if tag is None or tag.strip() == "":
        tag = ""
    return global_marshal("DEBUG_MESSAGE",
                          [simple_keyvalues_marshal("tag", tag),
                           simple_keyvalues_marshal("time", time),
                           simple_keyvalues_marshal("command", real_command)
                           ], "")
