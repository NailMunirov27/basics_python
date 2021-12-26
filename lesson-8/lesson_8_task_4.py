from functools import wraps


def val_checker(function):
    def checker(func):

        @wraps(func)
        def wrapper(num):
            if function(num):
                print(func(num))
            else:
                raise ValueError(f"wrong val {num}")

        return wrapper

    return checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(5)
except (ValueError, TypeError) as error:
    print(error)

# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
