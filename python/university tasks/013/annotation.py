def autrhor(name):
    def wrapper(func):
        def bob_check(*args):
            if name != 'bob':
                raise Exception('non-bobs not allowed')
            func(*args)
        return bob_check
    return wrapper

@autrhor('bobert')
def check_priviligies(a,b):
    print(a+b)

check_priviligies(2,5)
