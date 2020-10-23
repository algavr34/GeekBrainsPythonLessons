class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage" : wage, "bonus" : bonus}

class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя: {self.name} {self.surname}")

    def get_total_income(self):
        summa = self._income["wage"] + self._income["bonus"]
        print(f"Суммарный доход: {summa}")

first_person = Position("Евгений", "Пригожин", "Главред", 45000, 9666)
first_person.get_full_name()
first_person.get_total_income()
