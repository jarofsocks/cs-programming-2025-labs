ino = input()
if int(ino[-1]) % 2 == 0 and sum([int(i) for i in ino]) % 3 == 0:
    print('Делится на "6"')
else:
    print('Не делится на "6"')