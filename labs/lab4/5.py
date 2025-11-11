from pydoc import splitdoc
import string
pswrd = input('Введите пароль: ')
err_output = 'Пароль ненадежный: отсутствуют '
cnt = 0

for i in pswrd:
    if i in string.ascii_uppercase:
        cnt += 1
if cnt == 0:
    err_output += ', Заглавные буквы'
cnt = 0

for i in pswrd:
    if i in string.digits:
        cnt += 1
if cnt == 0:
    err_output += ', Строчные буквы'
cnt = 0

for i in pswrd:
    if i in string.punctuation:
        cnt += 1
if cnt == 0:    
    err_output += ', Специальные знаки'
        

if len(err_output) == 31: 
    print("Пароль надежный")
else: 
    print(err_output)
