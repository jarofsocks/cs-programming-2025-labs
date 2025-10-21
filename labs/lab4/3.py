ino = input('Введите возраст собаки (в годах): ')

import string
def error(a):
    if a[0] in string.ascii_letters:
        return 1
    elif int(a) < 1:
        return 2
    elif int(a) > 22:
        return 3

while 1:    
    if error(ino) == 1:
        print('Ошибка: возраст должен быть числом')
    elif error(ino) == 2:
        print('Ошибка: возраст должен быть не меньше 1')
    elif error(ino) == 3:
        print('Ошибка: возраст должен быть меньше 22')
    else:
        break

cnt = 0
for i in range(1,int(ino)+1):
    if i < 3:
        cnt += 10.5
    else:
        cnt += 4
print(f'Возраст собаки в человеческих годах: {cnt}')

