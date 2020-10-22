worker = {}
with open("hw_l5_task3_text.txt", "r") as file:
    for line in file:
        key, value = line.split()
        worker[key] = int(value)
print(f"Изначальный список работников: {worker}")
all_salary = 0
for key in worker:
     all_salary += worker[key]
     if worker[key] < 20000:
         print(f"Зарплата меньше 20к у {key}")
print(f"Средняя зарплата составляет: {int(all_salary / len(worker))}")