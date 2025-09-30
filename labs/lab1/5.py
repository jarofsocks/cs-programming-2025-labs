listy = []
for _ in range(3):
    listy.append(int(input()))
print(listy)
s = max(listy) * listy[1] / 2 
v = sum(listy)
print('s =',s)
print("v =",v)
