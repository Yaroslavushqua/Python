# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

n = int(input("Введите число: "))

sum = 1
numList = []

for i in range(n):
    sum *= i + 1
    numList.append(sum)

print(numList)