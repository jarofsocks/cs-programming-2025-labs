ino = input().lower().replace(' ', '')
half_len = int(len(ino) / 2)
if len(ino) % 2 != 0:
    ino = ino[:half_len] + ino[half_len + 1:]
if ino[:half_len] == ino[half_len:][::-1]:
    print('Да')
else:
    print('Нет')