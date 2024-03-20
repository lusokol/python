def all_thing_is_obj(object: any) -> int:
    types = {
        'list': 'List',
        'tuple': 'Tuple',
        'set': 'Set',
        'dict': 'Dict',
        'str': 'String'
    }
    obj_type = types.get(type(object).__name__, "Type not found")
    if (obj_type == "String"):
        print(f'{object} is in the kitchen : {type(object)}')
    elif (obj_type == "Type not found"):
        print(obj_type)
    else:
        print(f'{obj_type} : {type(object)}')
    return 42
