# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input("Введите число: "))
i = 2
list = []
num = n
while i <= n:
    if n % i == 0:
        list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(list)