#Задайте список, состоящий из произвольных чисел, количество задаёт 
# пользователь.Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).

sizeNum = int(input('Введите размер списка: '))
numList = []
sum = 0
for i in range(sizeNum):
     list_number = int(input(f'Введите число {i+1} '))
     numList.append(list_number)
     if i % 2 != 0:
         sum += numList[i]


print(numList)
print(f'Сумма чисел на нечетных позициях = {sum}')