import random

# print(random.random())
# num = 1
ch = "y"
while True:
    num = random.randint(1,6)
    if num == 1:
        print(' =========')
        print('|         |')
        print('|    0    |')
        print('|         |')
        print(' =========')
    elif num == 2:
        print(' =========')
        print('|         |')
        print('|  0   0  |')
        print('|         |')
        print(' =========')
    elif num == 3:
        print(' =========')
        print('|    0    |')
        print('|    0    |')
        print('|    0    |')
        print(' =========')
    elif num == 4:
        print(' =========')
        print('| 0     0 |')
        print('|         |')
        print('| 0     0 |')
        print(' =========')
    elif num == 5:
        print(' =========')
        print('| 0     0 |')
        print('|    0    |')
        print('| 0     0 |')
        print(' =========')
    elif num == 6:
        print(' =========')
        print('| 0     0 |')
        print('| 0     0 |')
        print('| 0     0 |')
        print(' =========')
    ch = input("Roll Again? Y/N: ")
    if ch.lower() != "y":
        print('exited :(')
        break
