import json

dict_for_firm = {}
count_profit = 0
profit = 0
middle_profit = 0
with open("hw_l5_task7_text.txt", "r") as file:
    for line in file:
        profit = float(line.split()[2]) - float(line.split()[3])
        dict_for_firm[line.split()[0]] = profit
        if profit > 0:
            count_profit += 1
            middle_profit += profit
list_for_json = [dict_for_firm, {"Our Profit": float(middle_profit / count_profit)}]
with open("hw_l5_task7.json", "x") as for_write:
    json.dump(list_for_json, for_write)