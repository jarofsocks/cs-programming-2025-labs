yr = input("Введите три числа: ").split()
min = yr[0]
for i in yr:
    if int(i) < min:
        min = int(i)
print(min)