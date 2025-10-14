ino = input('Введите температуру: ')
def tempo(x):
    x = int(x)
    if x < 20:
        return 'включён'
    else: 
        return 'выключен'
print(f'Кондиционер {tempo(ino)}')