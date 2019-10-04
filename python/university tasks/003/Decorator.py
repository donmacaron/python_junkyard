def decorator(func):
    def wrapper(*args):
        count = 1
        for i in args:
            if not isinstance(i, int):
                raise TypeError('None integer number found at %s position' % (count))
            count += 1
        return func(args)
    return wrapper


@decorator
def int_numbers(*args):
    for i in args:
        print(i)


int_numbers(1, 2, 3, 4, '2', 2, 3)
