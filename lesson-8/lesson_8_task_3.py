from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        list1 = [el for el in (*args, *kwargs.values())]
        n = [f"{func.__name__}({el}: {type(el)})" for el in list1]
        print(*n, *func(*args, *kwargs), sep=",\n")

    return wrapper


@type_logger
def calc_cube(*x, **y):
    list1 = [el for el in (*x, *y.values()) if isinstance(el, int) or isinstance(el, float)]
    return [i ** 3 for i in list1]


calc_cube(5, 11, A=5.66)
