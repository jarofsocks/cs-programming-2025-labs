while 1:
    ino = input().split(' ',1)
    input_money = int(ino[0])
    time_left = int(ino[1])
    stavka = 1
    if input_money < 30000:
        print('not enough money, try again (need at leats 30000)')
        continue
    else:
        break
stavka += input_money/10000*0.003
if stavka > 1.05:
    stavka = 1.05
money = input_money
for i in range(time_left):
    if i+1 <= 3:
        money *= stavka + 0.03
    elif i+1 <= 6:
        money *= stavka + 0.05
    elif i > 6:
        money *= stavka + 0.02
print(money-input_money, 2)