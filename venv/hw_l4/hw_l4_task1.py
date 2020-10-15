from sys import argv

script_name, work, rate, bonus = argv

print("Script name: ", script_name)
print("Your salary is: ", ((int(work) * int(rate)) + int(bonus)))