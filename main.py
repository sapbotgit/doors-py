import doors as d
import time
from art import tprint

tprint("DOORS")
print("Портировано SCS под питон (Сразу на русском")
print("(Не-графическая версия)")
a = input("Play Y\N? ")
if a == "Y":
    d.doors()

else:
    print("До следуещего запуска!")
    d.over("Exiter")

tprint("END of scripts")
time.sleep(5)
