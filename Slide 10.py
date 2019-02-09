import random
endgame='Да'
x=0
i=0
y=0
rounds=50
victory = random.randint(1, 100)
print('Подсказка: число = '+str(victory))
while x!=victory and endgame=='Да' and y<rounds:
    x = int(input('Угадайте число!'))
    y += 1
    if x==victory:
        endgame = input('Вы угадали! Хотите сыграть еще?')
        victory = random.randint(1, 100)
        print('Подсказка: число = '+str(victory))
        i+=1
    elif x<victory:
        print ('Нужно больше!')
    elif x>victory:
        print('Нужно меньше!')
if y>=rounds:
    print('Превышено кол-во попыток!')

print('Спасибо за игру! Кол-во игр: '+str(i))