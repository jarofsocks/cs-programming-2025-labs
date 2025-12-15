import random, string
listy = {string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase))-1] for i in range(20)}
listy = sorted(listy)
dicty = dict()
for i in range(len(listy)):
    dicty[listy[i]] = listy[i]
print(dicty.items())