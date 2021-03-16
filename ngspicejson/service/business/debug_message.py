from ..tool.marshal import global_marshal, simple_keyvalues_marshal


def make_debug_message(tag, real=False):
    return global_marshal("DEBUG_MESSAGE", simple_keyvalues_marshal("tag", tag), "")
