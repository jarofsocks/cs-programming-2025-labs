ino = int(input())
if int(str(ino)[-1]) % 2 == 0 and sum([int(i) for i in str(ino)]) % 3 == 0:
    print('Делится на "6"')
else:
    print('Не делится на "6"')