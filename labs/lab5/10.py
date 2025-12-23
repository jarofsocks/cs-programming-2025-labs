listy = [("Анна", [5, 4, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 5, 5])]
new_listy = {}
for i in listy:
    new_listy[i[0]] = round(sum(i[1])/len(i[1]))
print(new_listy.items())