def time_convert(x,y):
    from_x = x[-1] 
    x = int(x[0::-1])
    to_y = y
    listy = ['h','m','s']
    distance = (listy.index(from_x)) - (listy.index(to_y))
    for i in range(abs(distance)):
        if distance > 0:
            if i == 1:
                pass
            else:
                x /= 60
        else:
            x *= 60
    return str(x)+y
ino = input().split()
print(time_convert(ino[0],ino[1]))
