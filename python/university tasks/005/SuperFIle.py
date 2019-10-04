import os
import random
import string

class SuperFile():
    def __init__(self, name):
        self.name = ''
        if not os.path.isfile(name+'.txt'):
            self.name = name
            f = open(name+'.txt', 'w')
            N = 50
            f.write(''.join(random.choices(string.ascii_uppercase + string.digits, k=N)))
        else:
            # raise FileExistsError
            pass

    def inhale_data(self, file):
        path = file+'.txt'
        with open(path, 'r') as myfile:
            data=myfile.read().replace('\n', '')
        return data

    def string_mult(self, str, n):
        res = ''
        while n > 0:
            res += str
            n -= 1
        return res

    def __add__(self, f):
        f1 = self.inhale_data(self.name)
        f2 = self.inhale_data(f.name)
        f3 = open(self.name+f.name+'.txt', 'w')
        f3.write(f1+f2)
        f3.close()
        print('done')

    def __mul__(self, d):
        f1 = self.inhale_data(self.name)
        f3 = open(self.string_mult(self.name, d)+'.txt', 'w')
        f3.write(self.string_mult(f1, d))
        f3.close()
        print('done')




file_a  = SuperFile('Woody')
file_b = SuperFile('WoodPecker')

file_a * 3

file_c = file_a + file_b
