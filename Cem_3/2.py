# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке
# либо сообщит, что её нет.

from random import sample

def wordList (num, word="abc"):
    wList = []
    for i in range(num):
        n = sample(word, k=3)
        wList.append("".join(n))
    return wList

def fineSec (nList, word):
    if word in nList and nList.count(word)>1:
        c = nList.index(word)
        print(nList.index(word, c+1))
    else:
        print(-1)        

m = int(input("введите число: "))


u = wordList(m)
print(u)
n = input("Введите слово: ")
fineSec(u, n)