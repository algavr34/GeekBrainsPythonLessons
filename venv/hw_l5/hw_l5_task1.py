new_file = open("new_text_file.txt", "x")
with open("new_text_file.txt", "a") as file:
    while True:
        file.writelines(input("Напишите что-нибудь: ") + '\n')
        quit = input("Если хотите выйти, нажмите q. Если продолжаем, нажмите Enter: ")
        if quit == "q":
            break
with open("new_text_file.txt") as file:
    for line in file:
        print(line)