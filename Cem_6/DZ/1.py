# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.

from random import sample
len_list = int(input("Введите кол-во чисел в рандомном списке: "))
my_list = [i for i in sample(range(1, len_list*2), len_list)]
print("Рандомный список: ", my_list)
sort_list = [my_list[i]
             for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(sort_list)