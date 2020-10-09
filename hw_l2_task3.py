number = int(input("Write number of month from 1 to 12: "))
while number not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
    number = int(input("You're wrong! Write number of month from 1 to 12: "))
seasons1 = ["winter", "spring", "summer", "autumn"]
seasons2 = {1 : "winter", 2 : "spring", 3 : "summer", 4 : "autumn"}
if number in (12, 1, 2):
    print(f"It's {seasons1[0]}, i'm sure, it's {seasons2[1]}")
elif number in (3, 4, 5):
    print(f"It's {seasons1[1]}, i'm sure, it's {seasons2[2]}")
elif number in (6, 7, 8):
    print(f"It's {seasons1[2]}, i'm sure, it's {seasons2[3]}")
elif number in (9, 10, 11):
    print(f"It's {seasons1[3]}, i'm sure, it's {seasons2[4]}")