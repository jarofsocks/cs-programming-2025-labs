shifts = [6, 12, 8, 24, 10, 4]

some_shifts = list(filter(lambda x : x >= 8 and x <= 12, shifts))
for i in some_shifts:    
    print(i)