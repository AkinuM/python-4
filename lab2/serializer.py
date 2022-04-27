import inspect
from pydoc import locate

from constants import *


def get_type(item):
    itemtype = str(type(item))

    return itemtype[8:len(itemtype) - 2]


def serialize(item):
    if isinstance(item, (int, float, complex, bool, str, type(None))):
        return serialize_ifcbsn(item)
    if isinstance(item, (list, tuple, set, bytes)):
        return serialize_ltsb(item)
    if isinstance(item, dict):
        return serialize_dict(item)
    if inspect.isfunction(item):
        return serialize_function(item)
    if inspect.isclass(item):
        return serialize_class(item)
    if inspect.iscode(item):
        return serialize_code(item)
    if inspect.ismodule(item):
        return serialize_module(item)
    if inspect.ismethoddescriptor(item) or inspect.isbuiltin(item):
        return serialize_instance(item)
    if inspect.isgetsetdescriptor(item) or inspect.ismemberdescriptor(item):
        return serialize_instance(item)
    if isinstance(item, type(type.__dict__)):
        return serialize_instance(item)

    return serialize_object


def serialize_ifcbsn(item):
    result = {TYPE: get_type(item), VALUE: item}

    return result


def serialize_ltsb(item):
    result = {TYPE: get_type(item), VALUE: [serialize(obj) for obj in item]}

    return result


def serialize_dict(item):
    result = {TYPE: get_type(item), VALUE: [[serialize(key), serialize(item[key])] for key in item]}

    return result


def serialize_object(item):
    result = {TYPE: "object", VALUE: serialize({"__object_type__": get_type(item), "__fields__": item.__dict__})}

    return result


def serialize_function(item):
    # members = inspect.getmembers(item)
    # result = {TYPE: get_type(item)}
    # value = {}
    # for obj in members:
    #     if obj[0] in FUNC_ATTRIBUTES:
    #         value[obj[0]] = obj[1]
    #     if obj[0] == GLOBALS:
    #         value[GLOBALS] = {}
    #         for obj2 in obj[1]:
    #             if obj2 == item.__name__:
    #                 value[GLOBALS][obj2] = item.__name__
    #             else:
    #                 value[GLOBALS][obj2] = obj[1][obj2]

    # result[VALUE] = serialize(value)
    members = inspect.getmembers(item)
    result = {TYPE: get_type(item)}
    value = {}
    for obj in members:
        if obj[0] in FUNC_ATTRIBUTES:
            value[obj[0]] = (obj[1])
        if obj[0] == CODE:
            co_names = obj[1].__getattribute__("co_names")
            globs = item.__getattribute__(GLOBALS)
            value[GLOBALS] = {}
            for obj2 in co_names:
                if obj2 == item.__name__:
                    value[GLOBALS][obj2] = item.__name__
                elif obj2 in globs and not inspect.ismodule(obj2) and obj2 not in __builtins__:
                    value[GLOBALS][obj2] = globs[obj2]
    result[VALUE] = serialize(value)

    return result


def serialize_instance(item):
    members = inspect.getmembers(item)
    result = {TYPE: get_type(item), VALUE: serialize({obj[0]: obj[1] for obj in members if not callable(obj[1])})}

    return result


def serialize_code(item):
    if get_type(item) is None:
        return None

    members = inspect.getmembers(item)
    result = {TYPE: get_type(item), VALUE: serialize({obj[0]: obj[1] for obj in members if not callable(obj[1])})}

    return result


def serialize_module(item):
    tempitem = str(item)
    result = {TYPE: get_type(item), VALUE: tempitem[9:len(tempitem) - 13]}

    return result


def serialize_class(item):
    result = {TYPE: CLASS}
    value = {NAME: item.__name__}
    members = inspect.getmembers(item)
    for obj in members:
        if not (obj[0] in NOT_CLASS_ATTRIBUTES):
            value[obj[0]] = obj[1]
    result[VALUE] = serialize(value)

    return result


def deserialize(item):
    if item[TYPE] in [FLOAT, INT, COMPLEX, NONE_TYPE, BOOL, STRING]:
        return deserialize_ifcbsn(item)
    if item[TYPE] in [LIST, TUPLE, SET, BYTES]:
        return deserialize_ltsb(item)
    if item[TYPE] == DICT:
        return deserialize_dict(item)


def deserialize_ifcbsn(item):
    if item[TYPE] == NONE_TYPE:
        return None

    return locate(item[TYPE])(item[VALUE])


def deserialize_ltsb(item):
    if item[TYPE] == LIST:
        return list(deserialize(obj) for obj in item[VALUE])

    if item[TYPE] == TUPLE:
        return tuple(deserialize(obj) for obj in item[VALUE])

    if item[TYPE] == SET:
        return set(deserialize(obj) for obj in item[VALUE])

    if item[TYPE] == BYTES:
        return bytes(deserialize(obj) for obj in item[VALUE])


def deserialize_dict(item):
    return {deserialize(obj[0]): deserialize(obj[1]) for obj in item[VALUE]}
