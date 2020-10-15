from itertools import cycle, count
import time

for a in count(1):
    if a > 10:
        break
    else:
        print(f"Use count: {a}")
        time.sleep(1)

some_list = [1, 2, 3, 5, 7, 9]
c = cycle(some_list)
x = 0
while x < 10:
    print(next(c))
    x += 1