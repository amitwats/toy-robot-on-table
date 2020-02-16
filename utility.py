
def validateType(val,val_type):
    """
    This method determines of a particular 'val' is of a type 'val_type'.
    
    Arguments:
        val {any type} -- An object whose type needs to the assertained. The Type is taken from the next paramater.
        val_type {int|str|or any other data/object type} -- This is the type of object that the 'val' needs to be of.

        Raises:
        ValueError: If the expected object type of 'val' does not match 'val_type' then the exception is thrown.
    
    Returns:
        The type sent from 'val_type' -- This just returns thevalue passed if the value type is met. This can be consumed by the caller of the method.
    """
    if isinstance(val,val_type): return val
    raise ValueError(f"Expecting value of type '{val_type}' found {type(val)}")


def validateInteger(val):
    """Just validates if val is an integer type
    
    Arguments:
        val {int} -- An object that needs to essentially be an integer, failing which an exception is raised.

        Raises:
        ValueError: If the expected object type of 'val' is not of integer type.

    Returns:
        int -- If the 'val' is an integer type the same value is returned.
    """

    return validateType(val,int)

def validateString(val):
    """Just validates if val is a string type
    
    Arguments:
        val {str} -- An object that needs to essentially be an string, failing which an exception is raised.

        Raises:
        ValueError: If the expected object type of 'val' is not of string type.

    Returns:
        str -- If the 'val' is an string type the same value is returned.
    """
    return validateType(val,str)
