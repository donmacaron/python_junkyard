# already done
#     ls
#     cd
#     mkdir
#     open
#     copy
#     exit
#     supercopy
#
# todo
#     wget url                      (visualization)
#     wget url ext                  (скачать все файлы с расшринением ехt)
#     grep                          (поиск шалона в чем-то)  e.g. путь к файлу
#                                                           в папке, -r в под папках
#     makenote                      (создавать заметки, просматривать: всех, одной) edit: vi
#                                                                       новые окна: lib subprocess -> Popen
#
# notes: создание, просмотр. выводить номер, дату при просмотре и первую строку. rjust, ljust
# notes new создание
# notes просмотр всех заметок
# notes _num_ открывает заметку с указанным номером

# requests lib required



import os
import shutil
import datetime
import time
import re
import requests


print('Available commands: ls, cd, mkdir, open, copy, clear, help, exit')

def validate_supercopy(func):
    def wrapper(command):
        if not os.path.exists(command[0]):
            print("File %s not found" % (command[0]))
        elif not input_data[1].isdigit():
            print('% is not a number' % (command[1]))
        else:
            n = int(command[1])
            if n == 0:
                print('Cannot make zero copies')
            else:
                func(command)
    return wrapper


def validate_grep(func):
    def wrapper(command):
        reg = command[1]
        file = command[2]
        if len(command) == 4:
            if command[3] == '-r':
                option = True
            else:
                option = False
        if not os.path.exists(file):
            print('File/Dir does not exist')
        else:
            func(reg, file, option)
    return wrapper


def validate_path(func):
    def wrapper(*args):
        path = args[0]
        if len(args) == 1:
            if os.path.exists(path):
                return func(path)
            elif os.path.exists(os.getcwd()+path):
                return func(os.getcwd()+path)
            else:
                print('%s does not exist' % (path))
        elif len(args) == 2:
            if os.path.exists(path) and os.path.exists(args[1]):
                return func(path, args[1])
            else:
                print('%s does not exist' % (path))
    wrapper.__wrapped_fn = func
    return wrapper



def ls(returns=False):
    path = os.getcwd()
    print(path)
    file_list = []
    dir_list = []
    for f in os.listdir(path):
        if os.path.isfile(f):
            file_list.append(f)
        else:
            dir_list.append(f+"/")
    dir_guts = dir_list + file_list
    if returns:
        return dir_guts
    else:
        for g in dir_guts:
            print(g)

@validate_path
def cd(path):
    os.chdir(path)

def back():
    path = os.path.abspath(os.curdir)
    os.chdir('..')

def mkdir(path, name):
    if path == '':
        path = os.getcwd()
    if not os.path.exists(path+'\\'+name):
        os.makedirs(path+'\\'+name)
        print('Created %s at %s' % (name, path))
    else:
        print('There is already a dir with %s name' % (name))


@validate_path
def open(file):
    print('Opening %s' % (file))
    os.startfile(file)


@validate_path
def copy(file, path):
    shutil.copy(file, path)


@validate_path
def append(file):
    # print(file)
    f = os.path.abspath(os.curdir)+'\\'+file
    print(f)
    input_string = input('Add text to file:\n')
    mf = open(file, 'w')
    mf.write(input_string)
    mf.close()


def rm(regex):
    dir = os.getcwd()
    for f in os.listdir(dir):
        if re.search(regex, f):
            print(f)

    confirm = input('\nDelete files: [Y/N] ')

    if confirm == 'Y' or confirm == 'y':
        for f in os.listdir(dir):
            if re.search(regex, f):
                if os.path.isdir(f):
                    shutil.rmtree(f)
                else:
                    os.remove(os.path.join(dir, f))


@validate_supercopy
def supercopy(input_data):
    file = input_data[0]
    num = input_data[1]
    zeroes = len(num)
    n = int(num)
    k = file.rfind('.')
    for i in range(1, n + 1):
        file_name = file[:k] + str(i).zfill(zeroes) + '.' + file[k+1:]
        # copy(file, file_name)
        copy.__wrapped_fn(file, file_name)


def makenote(path):
    pass


@validate_grep
def grep(reg, file, option = False):
    print(option)



# test string for wget [url] [ext]
# wget http://www.3riversstadium.com/index2.html png

# test string for wget [url]
# wget http://toastytech.com/evil/billagram2.gif
def download_file(url):
    print('Downloading from ' + url)
    r = requests.get(url)
    f = url.split('/')[-1]
    path = os.getcwd()+'\\downloads\\'
    with open(path, 'wb') as file:
        file.write(r.content)
    print(f+' is downloaded\n')


def wget(url, ext=None):
    print('Downloading web-page...')
    page = requests.get(url)
    print('Done')
    print(type(ext))
    if isinstance(ext, str):
        reg = r'[h][t][t][A-Za-z0-9:/._-]*\.'+ext
        for f in re.findall(reg, page.text):
            download_file(f)
    else:
        download_file(url)


loop = True
while loop:
    print('\n'+os.path.abspath(os.curdir))
    command = input()
    split = command.split()
    if not split:
        continue

        # LS
    if split[0] == 'ls':
        ls()

        # CD
    if split[0] == 'cd':
        if len(split) == 2:
            cd(split[1])
        else:
            print('Incorrect number of arguments\n'+
                  'Hint: cd [path]')

            # MDKIR
    if split[0] == 'mkdir':
        if len(split) == 3:
            mkdir(split[1], split[2])
        elif len(split) == 2:
            mkdir('', split[1])
        else:
            print('Incorrect number of arguments\n'+
                  'Hint: mkdir [path] [name]\n'+
                  'or: mkdir [name]')

            # COPY
    if split[0] == 'copy':
        if len(split) == 3:
            copy(split[1], split[2])
        else:
            print('Incorrect number of arguments\n'+
                  'Hint: copy [file] [destination]')

            # OPEN
    if split[0] == 'open':
        if len(split) == 2:
            open(split[1])
        else:
            print('Incorrect number of arguments\n'+
                  'Hint: open [file]')

            # CLEAR
    if split[0] == 'clear':
        os.system('cls')

            # APPEND
    if split[0] == 'append':
        if len(split) == 2:
            append(split[1])
        else:
            print('Incorrect number of arguments\n'+
                  'Hint: append [*.txt]')

                 # RM
    if split[0] == 'rm':
        if len(split) == 2:
            rm(split[1])
        else:
            print('Incorrect number of arguments\n'+
                  'Hint: rm [regexp]')

                  # BACK
    if split[0] == 'back':
        back()

                # SUPERCOPY
    if split[0] == 'supercopy':
        if len(split) != 3:
            print('Incorrect number of arguments')
        else:
            input_data = []
            input_data.append(split[1])
            input_data.append(split[2])
            # supercopy(split[1], split[2])
            supercopy(input_data)

                # GREP
    if split[0] == 'grep':
        if len(split) < 2:
            print('Incorrect number of arguments')
        else:
            grep(split[1], split[2])


                # WGET
    if split[0] == 'wget':
        if len(split) == 3:
            wget(split[1], split[2])
        else:
            wget(split[1])

            # EXIT
    if split[0] == 'exit':
        print('exiting..')
        loop = False

            # HELP
    if split[0] == 'help':
        print('Available commands: \n'+
        'ls - shows content of current directory\n'+
        'cd [path] - changes current directory\n'+
        'back - goes upper in the dir tree\n'+
        'mkdir [path] [name] - creates at given path\n'+
        'open [file] - opens file with default program for this file\n'+
        'copy [file] [destination] - copies selected file to given path\n'+
        'supercopy [file] [number of copies] - description\n'+
        'grep [] - description\n'+
        'rm [regexp] - deletes everything that mathes regexp\n'+
        'exit - exit from program')
