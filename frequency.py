# -*- coding: utf-8 -*-
# Бабушкина Н. В., 05-703, Подсчёт встречаемости символов в строке

s=input('Введите строку:\n')
dic={} # создание пустого словаря
for ch in s:# цикл, который проходит по каждому символу строки
    if ch in dic:
        dic[ch]+=1 # если символ ch(ключ в словаре) есть в словаре dic,
# то прибавляем 1
    else:
        dic[ch]=1 # иначе считаем как первое вхождение символа
for key, value in dic.items():
    print(key, value, sep='-') # вывод пары ключ-значение