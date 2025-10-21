hour = int(input('Введите час (0–23): '))
if hour < 5:
    print('Сейчас утро')
elif 4 < hour < 12:
    print('Сейчас день')
elif 11 < hour < 18:
    print('Сейчас вечер')
elif 17 < hour < 24:
    print('Сейчас ночь')
elif hour > 23:
    print('Ошибка')
