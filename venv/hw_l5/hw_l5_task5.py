with open("hw_l5_task5_text.txt", "x") as file:
    file.write(input("Введите несколько чисел через пробел: "))
with open("hw_l5_task5_text.txt", "r") as file:
    numbers = file.readline().split()
    for index, item in enumerate(numbers):
        numbers[index] = float(item)
    print(f"Наш лист из введённых чисел: {numbers}")
    summa = 0
    for i in numbers:
        summa += i
    print(f"Сумма введённых чисел: {summa}")