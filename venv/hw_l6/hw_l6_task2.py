class Road:

    def __init__(self, length, width, mass_for_one, depth):
        self.length = int(length)
        self.width = int(width)
        self.mass_for_one = int(mass_for_one)
        self.depth = int(depth)

    def mass(self):
        mass = self.length * self.width * self.mass_for_one * self.depth
        return mass

vlg_msc = Road(int(input("Введите длинну дороги: ")),
               int(input("Введите ширину дороги: ")),
               int(input("Введите массу асфальта на 1 кв. км дороги: ")),
               int(input("Введите толщину слоя асфальта: ")))
print(f"Нужна следующая масса асфальта: {vlg_msc.mass()} кг")