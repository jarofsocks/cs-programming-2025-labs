from http.client import SWITCHING_PROTOCOLS


price = int(input('Введите сумму покупки: '))
i = 0
if price < 1000:
    i = 0
elif 999 < price < 5001:
    i = 0.05
elif 4999 < price < 10001:
    i = 0.10
elif 10000 < price:
    i = 0.15
print(f'Ваша скидка: {i*100}%', f'К оплате: {price - price * i}', sep = '\n')
