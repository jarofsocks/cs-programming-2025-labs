dicty = {"milk": 100, "vine": 1000, "meat": 300, "cheese": 350}
mini, maxi, min_name, max_name = dicty["milk"], dicty["milk"], "milk", "milk"
for i, j in dicty.items():
    if j < mini:
        mini = j
        min_name = i
    if j > maxi:
        maxi = j
        max_name = i
print(f'min -> {min_name}, max -> {max_name}')