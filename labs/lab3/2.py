num = 0
while num < 1 or num > 9: 
    print("Напиши число от 1 до 9")
    num = int(input())
for i in range(1,11):    
    print(f"{i} * {num} = {i*num}")