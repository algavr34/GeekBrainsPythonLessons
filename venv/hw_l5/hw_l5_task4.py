key_for_new_text = {"One" : "Один",
                    "Two" : "Два",
                    "Three" : "Три",
                    "Four" : "Четыре"}
with open("hw_l5_task4_text.txt", "r") as file:
    with open("hw_l5_task4_newtext.txt", "x") as new_file:
        old_list = file.readlines()
        for line in old_list:
            new_list = line.split(" - ")
            new_file.write(f"{key_for_new_text[new_list[0]]} - {new_list[1]}")