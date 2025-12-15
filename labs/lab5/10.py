listy = [("Анна", [5, 4, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 5, 5])]
new_listy = {}
for i in listy:
    new_listy[i[0]] = sum(i[1])/len(i[1])
for i, j in new_listy.items():
    max = new_listy["Анна"]
    if j > max:
        max_name = i
        max = j
print(f'{max_name} имеет наивысший средний балл: {max}')