while 1:    
    ino = int(input('Введите возраст собаки (в годах): '))
    if ino > 0:
        break
    print('Ошибка: возраст должен быть не меньше 1')
cnt = float(0)
for i in range(1,ino+1):
    if i < 3:
        cnt += 10.5
    else:
        cnt += 4
print(f'Возраст собаки в человеческих годах: {cnt}')

