<<<<<<< Updated upstream
ino = input()
if int(ino[-1]) % 2 == 0 and sum([int(i) for i in ino]) % 3 == 0:
=======
ino = int(input())
if int(str(ino)[-1]) % 2 == 0 and sum([int(i) for i in str(ino)]) % 3 == 0:   
>>>>>>> Stashed changes
    print('Делится на "6"')
else:
    print('Не делится на "6"')