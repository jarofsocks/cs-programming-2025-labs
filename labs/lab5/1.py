from tkinter import N


listy = [1, 54, 87, 23, 65, 76, 987, 3, 1, 11]
new_listy = [int(str(i).replace('3',"30")) for i in listy]
print(new_listy)