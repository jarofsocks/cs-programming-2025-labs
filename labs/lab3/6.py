fib = [0,1]
for i in range(int(input())):
    fib.append(fib[i]+fib[i+1])
print(*fib)