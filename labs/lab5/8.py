import random
user_inp = input('Выберите: Камень  Ножницы  Бумага  Ящерица  Спок (1-5)')
enemy_inp = random.randint(1,5)
who_beats_who = {1:{2,4}, 2:{3,4}, 3:{1,5}, 4:{3,5}, 5:{1,2}}
if enemy_inp in who_beats_who[user_inp]:
    print('Вы победили!')
else:
    print('Вы проиграли!')