# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

max_num = int(input("Введите максимальное число в списке: "))
my_list = [i for i in range(20, (max_num + 1)) if i % 20 == 0 or i % 21 == 0]
print(f"Список чисел от 20 до {max_num} кратных 20 или 21: ", my_list)