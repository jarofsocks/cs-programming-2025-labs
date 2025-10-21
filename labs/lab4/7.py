yr = input("Введите три числа: ").split()
min = 9999999999999
for i in yr:
    if int(i) < min:
        min = int(i)
print(min)