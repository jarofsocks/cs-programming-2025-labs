ino = input()
if ino[::len(ino)/2] == ino[len(ino)/2::]:
    print('Да')
else:
    print('Нет')