#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re


# 1) надо опредилить тип слова:
#     сколько резать с начала слова и куда писать "хйу"
# 2) отрезать слово согласно его типу
# 3) приписать "хйу"
# words = ['кот', 'поезд', 'лес', 'оправа',
#         'меланхолия', 'вилка', 'жопа', 'мясо',]
#
# vowels = ('а', 'е', 'ё', 'и', 'й', 'о', 'у','э', 'ю', 'я')
# consonants = ('б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н',
#             'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'щ', 'ш',)

# собака - хуе бака

def rhyme(word):
    single_prn = ('я', 'ты', 'он', 'она', 'оно')
    plural_prn = ('они', 'мы', 'вы')
    templ = 'хуй'
    if word in single_prn:
        return templ
    elif word in plural_prn:
        return templ[:2] + 'и'
    if len(word) > 1:
        if (word[1:][0] == 'и') or (word[1:][0] == 'е'):
            return templ[:2] + word[1:]
        elif word[1:][0] == 'о':
            return templ[:2] + 'е' + word[2:]
        elif word[1:][0] == 'у':
            return templ[:2] + 'ю' + word[2:]
        elif word[1:][0] == 'а':
            return templ[:2] + 'я' + word[2:]
    return templ + word[1:]


def is_cyrillic(word):
    return bool(re.search('[а-я]', word))


def main_cycle():
    cycle = True
    print('Вводи слово кириллицей, малолетний дебил.\nпечатай "выход" чтобы прекратить мучения')

    while(cycle):
        word = input()
        if is_cyrillic(word):
            if word != 'выход':
                print('%s - %s' % (word, rhyme(word)))
            else:
                cycle = False
        else:
            print('Vvodi po-ruuske, hu-u-ske! Russke vpered!1 >:O')

    print('Вот такие дела, засранцы - %s' % rhyme('засранцы'))


# for w in words:
#     print('%s - %s' % (w, rhyme(w)))

main_cycle()
