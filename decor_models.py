def decor_reality(func):
    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return new_func

val_count = 0
session_number = 0

def session_counter(refunc):
    def wrapper_1(*args, **kwargs):
        global session_number
        session_number += 1
        print(session_number, "количество сессий")
        return refunc(*args, **kwargs)
    return wrapper_1

def validate_couter(valfunc):
    def wrapper_2(*args, **kwargs):
        global val_count
        val_count += 1
        print(val_count, "число для валидации")
        return valfunc(*args, **kwargs)
    return wrapper_2

def name_func_panel(func):
    def new_func(*args, **kwargs):
        result = func.__name__
        func(*args, **kwargs)
        return result
    return new_func