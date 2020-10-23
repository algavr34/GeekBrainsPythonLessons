from time import sleep

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f"{self.name} поехала!")

    def stop(self):
        print(f"{self.name} остановилась!")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}")

    def show_speed(self):
        print(f"Cкорость {self.name}: {self.speed}")

class TownCar(Car):
    def show_speed(self):
        print(f"Cкорость {self.name}: {self.speed}")
        if self.speed > 60:
            print(f"{self.name} превышает скорость!")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f"Cкорость {self.name}: {self.speed}")
        if self.speed > 40:
            print(f"{self.name} превышает скорость!")

class PoliceCar(Car):
    def is_police(self):
        self.is_police = True
        print(self.is_police)

typical_town_car = TownCar(55, "yellow", "Modesto", False)
typical_town_car.go()
typical_town_car.stop()
typical_town_car.turn("Налево")
typical_town_car.turn("Направо")
typical_town_car.show_speed()
sleep(5)

bad_town_car = TownCar(65, "yellow", "ModestoII", False)
bad_town_car.go()
bad_town_car.stop()
bad_town_car.turn("Налево")
bad_town_car.turn("Направо")
bad_town_car.show_speed()
sleep(5)

typical_sport_car = SportCar(100, "red", "PickleRick", False)
typical_sport_car.go()
typical_sport_car.stop()
typical_sport_car.turn("Налево")
typical_sport_car.turn("Направо")
typical_sport_car.show_speed()
sleep(5)

typical_work_car = WorkCar(39, "white", "BoringDude", False)
typical_work_car.go()
typical_work_car.stop()
typical_work_car.turn("Налево")
typical_work_car.turn("Направо")
typical_work_car.show_speed()
sleep(5)

bad_work_car = WorkCar(41, "white", "NotBoringDude", False)
bad_work_car.go()
bad_work_car.stop()
bad_work_car.turn("Налево")
bad_work_car.turn("Направо")
bad_work_car.show_speed()
sleep(5)

typical_police_car = PoliceCar(77, "white", "Lega", False)
typical_police_car.go()
typical_police_car.stop()
typical_police_car.turn("Налево")
typical_police_car.turn("Направо")
typical_police_car.show_speed()
typical_police_car.is_police()
print(typical_police_car.is_police())