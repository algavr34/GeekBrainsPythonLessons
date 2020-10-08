list = input("Enter the elements of the first list separated by a space and then press Enter: ").split(" ")
print(list)
for i in range(1, len(list), 2):
    list[i - 1], list[i] = list[i], list[i - 1]
print(list)
