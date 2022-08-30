import random

arr = []
for _ in range(1000000):
    if random.randrange(0, 10) <= 2:
        arr.append(str(0))
    else:
        arr.append(str(random.randrange(0, 1000)))

with open('close_zero/data.txt', mode='w') as my_file:
    my_file.write('1000000\n' + ' '.join(arr))
