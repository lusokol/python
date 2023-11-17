def NULL_not_found(object: any) -> int:
    types = {
        'NoneType' : 'Nothing',
        'float' : 'Cheese',
        'int' : 'Zero',
        'str' : 'Empty',
        'bool' : 'Fake'
    }
    obj_type = types.get(type(object).__name__)
    if obj_type == "Empty" :
        if object == '' :
            print(f'{obj_type}: {type(object)}')
        else :
            print(f"Type not found")
            return 1
    elif ((obj_type == "Zero" and object != 0) or (obj_type == "Fake" and object != False)) :
        print(f"Type not found")
    else :
        print(f'{obj_type}: {object} {type(object)}')
    return 0