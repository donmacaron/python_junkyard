import random


def int_to_rom(func):
    """ This method coverts integers to roman numbers """
    def to_rom(num):
        res = []
        roms = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        n = len(roms)
        i = 0
        while not i == n:
            c = int(num / ints[i])
            res.append(roms[i]*c)
            temp = ints[i] * c
            num -= temp
            i += 1
        rom_num = ''
        for i in res:
            rom_num += i
        return rom_num
    """ This wrapper checks if input data is acceptable for converting
        and if it is, starts converting,
        or returns original value                                   """
    def wrapper(*args):
        try:
            num = int(func(*args))
        except Exception:
            num = -1
        if 0 < num < 4000:
            res = to_rom(num)
        else:
            res = func(*args)

        return res
    return wrapper


@int_to_rom
def bobot(a, b):
    return a + b


def test():
    roms = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    d = {k: v for k, v in zip(reversed(roms), reversed(ints))}
    print(d)
    i = 10
    while i > 0:
        r1 = random.randrange(1, 100)
        r2 = random.randrange(1, 100)
        print('r1: %s, r2: %s\nr1 + r2 = %s' % (r1, r2, r1 + r2))
        print(bobot(r1, r2))
        print('')
        i -= 1


test()
