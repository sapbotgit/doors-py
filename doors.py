from art import tprint
import time, random

random.seed(1)
rooms = ['EmptyRoom']
glitches = 0
def door(a):
    glitch = False
    tprint(string(a))
    if a == 1:
        print('Перед вами ключ... вы его берёте и подходите к двери...')
    else:
        room = random.choice(rooms)
        if room == 'EmptyRoom':
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
        
