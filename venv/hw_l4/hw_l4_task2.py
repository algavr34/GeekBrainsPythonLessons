from random import randint

start_list = [randint(1, 100) for _ in range(10)]
print(f"Start list: {start_list}")
new_list = []
for i in range(len(start_list) - 1):
    if start_list[i + 1] > start_list[i]:
        new_list.append(start_list[i + 1])
print(f"New list: {new_list}")