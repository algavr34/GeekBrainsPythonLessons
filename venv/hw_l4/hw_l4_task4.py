start_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(start_list)
new_list = []
for i in start_list:
    if start_list.count(i) == 1:
        new_list.append(i)
print(new_list)