class Cell:
    def __init__(self, size : int):
        self.size = size

    def __add__(self, other):
        return f"Результат сложения клеток: {self.size + other.size}"

    def __sub__(self, other):
        if self.size - other.size > 0:
            return f"Результат вычитания клеток: {self.size - other.size}"
        else:
            return "Вычесть клетки невозможно!"

    def __mul__(self, other):
        return f"Результат умножения клеток: {self.size * other.size}"

    def __truediv__(self, other):
        return f"Результат деления клеток: {self.size // other.size}"

    def make_order(self, len):
        vyvod = ""
        for i in range(self.size // len):
            vyvod += "*" * len + "\n"
        vyvod += "*" * (self.size % len) + "\n"
        return vyvod

first_cell = Cell(12)
second_cell = Cell(15)
print(first_cell + second_cell)
print(first_cell - second_cell)
print(first_cell * second_cell)
print(first_cell / second_cell)
print(first_cell.make_order(7))
