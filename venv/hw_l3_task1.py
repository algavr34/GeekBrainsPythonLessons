def split():
    global a, b
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        return
    res = (a / b).__round__(2)
    return res

print(f"You'result is {split()}")
