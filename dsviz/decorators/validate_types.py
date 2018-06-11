'''Validate types decorator.'''


def validate_types(allowed_types):
    '''A decorator for a data structure's constructor to validate the type of
    data being stored.

    Args:
        allowed_types: A set of allowed types for the data structure.

    Raises:
        TypeError: If the data type is not supported by the data structure or if
            there are missing positional arguments.
    '''
    def decorator(func):
        def check_types(*args):
            if len(args) < 3:
                raise TypeError('Missing positional arguments: \'name\' and \'data_type\'')
            data_type = args[2]
            if data_type not in allowed_types:
                raise TypeError('Data type is not supported by this data structure.')
            return func(*args)
        return check_types
    return decorator
