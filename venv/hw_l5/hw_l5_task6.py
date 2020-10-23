import re

with open("hw_l5_task6_text.txt", "r") as file:
    all_lessons = list()
    lessons = list()
    for line in file:
        all_lessons.append(str(re.findall(r"\w+\:", line)))
        lessons.append(sum(map(int, re.findall(r"\d+", line))))
    our_list = {all_lessons[i]: lessons[i] for i in range(len(all_lessons))}
    print(our_list)