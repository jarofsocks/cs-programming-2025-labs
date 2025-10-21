yr = int(input("Введите год: ")) 
if yr % 4 == 0 and not(yr % 100 == 0) or yr % 400 == 0:
    print(f'{yr} - Високосный год')
else:
    print(f'{yr} - Не високосный год')
