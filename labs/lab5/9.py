listy = ["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]
new_listy = {}
for i in [j[0] for j in listy]:
    new_listy[i] = []
for i in new_listy:
    for k in listy:
        if i == k[0]:
            new_listy[i].append(k)
print(new_listy.items())   