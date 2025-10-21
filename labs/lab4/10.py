import string

while 1:
    num = input('Введите число: ')
    if num[0] in string.ascii_letters:
        print('Ошибка: input не является числом')
    elif int(num) < 1:
        print('Ошибка: input меньше 1')
    elif int(num) * 1 == int(num) and int(num) > 0:
        break

divs = 0 
num = int(num)

for i in range(1,num+1):
    if num % i == 0:
        divs += 1

if num >= 1 and divs <= 2:
    print(f'{num} - простое число')
else:
    print(f'{num} - составное число')