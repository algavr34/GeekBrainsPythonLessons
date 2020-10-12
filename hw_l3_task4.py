def my_func(x, y):
    return x ** y

def my_func_2(x, y):
    r = 1
    if y > 0:
        while y > 0:
            r *= x
            y -= 1
    elif y < 0:
        y = abs(y)
        while y > 0:
            r *= x
            y -= 1
        r = 1 / r
    else:
        x = 1
    return r

number = float(input("Enter number: "))
power = int(input("Enter power: "))
print(f"Result: {my_func(number, power)} with **")
print(f"Result: {my_func_2(number, power)} with while")
