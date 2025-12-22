from decimal import MIN_EMIN


dicty = {"milk": 100, "vine": 1000, "meat": 300, "cheese": 350}
min, max = 2*128, 0
for i, j in dicty.items():
    if j < min:
        min_name = i
    if j > max:
        max_name = i
print(f'min -> {min_name}, max -> {max_name}')