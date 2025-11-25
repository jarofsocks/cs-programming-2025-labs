dicty = {
    'apple':'яблоко',
    'pencil':'карандаш',
    'milk':'молоко',
    'chocolate':'шоколад',
    'coffee':'кофе',
    'number':'число',
    'family':'семья',
    'meme':'мем'
}
ino = input(f'Words we can translate: {dicty.values()}, please enter your word: ')
for i,j in dicty.items():
    if j == ino:
        print(i)
        break 