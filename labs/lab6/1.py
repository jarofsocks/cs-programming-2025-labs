ino = input().split(' ',1)
nume = int(ino[0][:-1])
frome = ino[0][-1]
toe = ino[1]
times = ['s','m','h']
diff = times.index(toe) - times.index(frome)

while diff != 0:
    if diff > 0:
        diff -= 1
        nume /= 60
    elif diff < 0:
        diff += 1
        nume *= 60
    else:
        break

print(str(round(nume, 3))+toe)
