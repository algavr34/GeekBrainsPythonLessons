first = int(input("Введите, сколько вы пробежали в первый день: "))
maximum = int(input("Введите, сколько вы хотите пробегать: "))
days = 1
while maximum >= first:
    print("День", days, ":", first)
    first = first * 1.1
    days = days + 1
print(f"На {days} день вы достигнете показателя в {first} км")
