number = 0
my_list = [7, 5, 3, 3, 2]
print(f"Start rate is {my_list}")
while number != 999:
    number = int(input("Write some number. If you want stop, write '999': "))
    if number == 999:
        break
    else:
        my_list.append(number)
        my_list.sort(reverse=True)
        print(f"Now rate is {my_list}")
