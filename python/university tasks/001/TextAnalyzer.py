import string
import random
from collections import OrderedDict


files = ('palpatine', 'tom_of_strahd', 'test')
def analyze():
    # abc = dict.fromkeys(string.ascii_lowercase, 0)
    abc = {}
    fname = files[random.randrange(len(files))]
    with open(fname +'.txt', 'r', encoding='utf8') as file:
        text = file.read().lower()

    print('Opened %s file' % (fname))

    for n in text:
        k = abc.keys()
        if n in k:
            abc[n] += 1
        else:
            abc[n] = 1

    abc = OrderedDict(sorted(abc.items()))
    for k, v in abc.items():
        print(k, v)
    return abc


analyze()
