# 2. Создать список, длины n, значения формируются по формуле 3k + 1,
# где k принимает значения от 1 до n включительно.

numList = []
n = int(input("Введите число: "))
for k in range(1,n+1):
    numList.append(3*k+1)
print(numList)