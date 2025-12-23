import string
corty = (1, 14, 5, 9, 'sadas', 32)
flagy = True
for i in corty:
    if [j in str(i) for j in string.ascii_lowercase + string.ascii_uppercase]:
        flagy = False
if flagy == True:    
    new_corty = tuple(sorted(corty))
else:
    new_corty = corty
print(new_corty)