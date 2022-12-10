from art import tprint
import time
def door():
    print("Это не доработано")
    
def doors():
    print("Добро пожаловать в DOORS...")
    time.sleep(3)
    door()

def over(monster):
    tprint("YOU DIED!")
    time.sleep(3)
    print("Вас убил " + monster)
    time.sleep(5)
    if monster == "Rush":
        print("Если пришёл Rush попробуйте спрятатся в шкаф")

    if monster == "Exiter":
        print("Если вы не хотите быть убитым Exiter'ом:")
        print("Не выходите из игры пока не зайдёте в игру")

    if monster == "Non-wanter":
        print("Non-wanter убивает когда долгий выбор")
        
