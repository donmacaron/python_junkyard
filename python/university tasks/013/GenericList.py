    #
    # None
    # bool
    # int
    # float
    # complex
    # str
    # list
    # tuple
    # set
    # dict
    #

class generic_list(object):
    def __init__(self, type):
        self.type = type
        self.lst = []
        # print('class type is %s' % (type))

    def add(self, input):
        if isinstance(input, self.type):
            self.lst.append(input)

    def print(self):
        for i in self.lst:
            print(i)


junk_list = [0, 1.0, 'str', [2,2], {'aaaa' : 1}, 21, '21', (1,2,3), True]

my_list = generic_list(int)
for i in junk_list:
    my_list.add(i)

my_list.print()
