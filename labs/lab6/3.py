ino = input().split(' ', 1)

if int(ino[1]) < int(ino[0]):
    print('Error!')

cnt = 0
for num in range(int(ino[0]),int(ino[1])):
    devs = 0
    for i in range(1,int(num**0.5)+1):    
        if num % i == 0:
            devs += 1
    if devs == 1:
        if num == 1:
            continue
        print(num, end = ' ')
        cnt += 1

if cnt == 0:
    print('Error!')