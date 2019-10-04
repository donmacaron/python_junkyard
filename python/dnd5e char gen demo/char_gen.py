import codecs
from character import *
from classes import *


def show_text(x=0, flag='DEFAULT_FLAG'):
    text = 'intro.txt'
    with open(text, encoding='utf-8') as fp:
        fp.seek(x)
        line = fp.readline()
        cnt = 1
        while line:
            if line.find(flag) is not -1:
                x = fp.tell()
                fp.close()
                return x
                break
            print(line, end=' ')
            line = fp.readline()
            cnt += 1

def create_character():
    text = show_text(0, '_name')
    char_name = input()
    text = show_text(text, '_class')
    class_num = int(input())
    if 1 <= int(class_num) <= 12:
        classes = {1:Bard(), 2:Barbarian(), 3:Fighter(), 4:Wizard(), 5:Druid(),
                   6:Cleric(), 7:Warlock(), 8:Monk(), 9:Paladin(), 10:Rogue(),
                   11:Ranger(), 12:Sorcerer()}
        char_class = classes[class_num]
    print('Вы выбрали следующий класс: '+ char_class.name)
    char_race = input('Напишите свою расу\n')
    ab_scores = {'str': 0, 'dex': 0, 'con': 0,
                      'int': 0, 'wis': 0, 'cha': 0}
    text = show_text(text, '_ab_score')
    for k, v in ab_scores.items():
        ab_scores[k] = int(input(k+': '))

    text = show_text(text, '_race_scores')
    a = True
    while a:
        race_scores = input().split()
        ab_scores[race_scores[0]] += int(race_scores[1])
        if input('Еще? (y/n)') == 'n':
            a = False


    char = Character(char_name, char_class, char_race, ab_scores)

    with open(char_name+'.txt', 'w+') as char_file:
        char_file.write(char.charsheet_fill())




create_character()
