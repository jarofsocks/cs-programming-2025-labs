from pydoc import splitdoc
import string
pswrd = input('Введите пароль: ')
err_output = 'Пароль ненадежный: отсутствуют '

upprcase = False
for i in pswrd:
    if i in string.ascii_uppercase:
        upprcase = True

nmbrs = False
for i in pswrd:
    if i in string.digits:
        nmbrs = True

splc = False
for i in pswrd:
    if i in string.punctuation:
        splc = True

