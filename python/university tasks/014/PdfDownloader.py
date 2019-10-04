import os
import requests
import re

# pip install requests
# 0. скачать файл
# 1. по url скачать все файлы с заданным расширением
# 2. скачать все файлы многопоточно
# скачивает страницу -> а потом pdf файлы с этой страницы

def download_file(url): #загружает один файл
    print('downloading from '+ url)
    r = requests.get(url)
    f = url.split('/')[-1]
    # path = 'C:\\Projects\\python\\study\\REQUESTS_STUDY'+'\\'+ str(f)
    path = os.getcwd()+'\\downloads\\'+str(f)

    with open(path, 'wb') as file:
        file.write(r.content)
    print(f+' is downloaded\n')


def download_page():
    url = 'http://www.3riversstadium.com/index2.html'
    # url = 'https://en.wikipedia.org/wiki/2019_redefinition_of_SI_base_units'
    r = requests.get(url)
    print('done\n')
    return r.text


def find_files():
    print('downloading web-page')
    text = download_page()
    # reg = r'[h][t][t][A-Za-z0-9:/._-]*\.gif'
    reg = r'"h(\S)+.png"'
    for f in re.findall(reg, text):
        print(f)
        download_file(f)



find_files()
