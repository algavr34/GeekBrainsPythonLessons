class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запись отрисовки"

class Pen(Stationery):

    def draw(self):
        return f"{super().draw()}. Пишем и помним, что это нифига не сотрётся"

class Pencil(Stationery):

    def draw(self):
        return f"{super().draw()}. Пишем и помним, что мы можем всё стереть! Только найдите хороший ластик :)"

class Handle(Stationery):

    def draw(self):
        return f"{super().draw()}. Пишем и ни в коем случае не нюхаем!"

pen = Pen("Ручка")
print(pen.draw())

pcl = Pencil("Карандаш")
print(pcl.draw())

marker = Handle("Особо токсичный маркер")
print(marker.draw())

some_write = Stationery("Хз что это")
print(some_write.draw())