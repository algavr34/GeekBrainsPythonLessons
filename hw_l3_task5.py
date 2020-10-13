a = 0
try:
    while True:
        for n in map(int, input("Write numbers separated by space. If you want stop, enter 'q': ").split(" ")):
            a += n
            print(a)
except ValueError:
    print(a)
