from art import tprint
import time, random, sys

random.seed(1)
rooms = ['Glitch']
glitches = 0
def door(a):
    glitch = False
    tprint(str(a))
    if a == 1:
        print('Перед вами ключ... вы его берёте и подходите к двери...')
    elif a == 50:
        print('''Пароль состоиз из 5 цифр
1 - Это треугольник
2 - Квадрат
3 - Круг
4 - Ромб
5 - Крест

Квадрат это 6
Треугольник это 9
Круг это 5
Ромб это 2
Крест это 1

Какой пароль?''')
        if input('Пароль: ') == '96321':
            print('Поздравляю вы выжили!')
        else:
            print('Вы ввели неверный пароль')
            over('Figure')
    else:
        rm = random.choice(rooms)
        if rm == 'EmptyRoom':
            print('Вам повезло! Эта комната пустая и тут никого нет!')
        else:
            print('Ох что-то пошло не так и вас телепортировал глитч!')
            glitch += 1
            if glitch >= 3:
                over('Glitch')
    if not glitch:
        newdoor()
def newdoor():
    print('Нажмите Enter чтобы открыть дверь...')
    input('')
def doors():
    print("Добро пожаловать в DOORS...")
    time.sleep(3)
    for room in range(100):
        door(room + 1)

def over(monster):
    tprint("YOU DIED!")
    time.sleep(3)
    print("Вас убил " + monster)
    time.sleep(5)
    if monster == "Rush":
        print("Если пришёл Rush попробуйте спрятатся в шкаф")

    elif monster == "Exiter":
        print("Если вы не хотите быть убитым Exiter'ом:")
        print("Не выходите из игры пока не зайдёте в игру")

    elif monster == "Non-wanter":
        print("Non-wanter убивает когда долгий выбор")
    elif monster == "Glitch":
        print('Не бойтесь! Вы никак не влияли на него. Это - ошибка игры...')
    else:
        print('Странно... вас убил монстр которого не существует...')
        input('Нажмите Enter тобы выйти...')
        sys.exit()
