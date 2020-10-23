from time import sleep
from itertools import cycle

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        count = 0
        colors = ["красный", "жёлтый", "зелёный", "жёлтый"]
        for el in cycle(colors):
            if count > 6:
                print("На сегодня всё!")
                break
            if colors.index(el) % 2 == 0:
                print(f"Сейчас горит {el}")
                sleep(7)
            else:
                print(f"Сейчас горит {el}")
                sleep(2)
            count += 1

my_traffic_light = TrafficLight("1")
print(my_traffic_light.running())