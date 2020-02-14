
def validateType(val,val_type):
    if isinstance(val,val_type): return val
    raise ValueError(f"Expecting value of type '{val_type}' found {type(val)}")


def validateInteger(val):
    return validateType(val,int)

def validateString(val):
    return validateType(val,str)
