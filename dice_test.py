import random

count = 0
flag = False
all_count = 1
max_offset = 0
while flag is False:
    for i in range(315672):
        y = random.randrange(1, 7, 1)
        if y == 5 or y == 6:
            count += 1
    if count >= 106602 or count <= 103846:
        print(all_count)
        print(count)
        flag = True
    else:
        offset = abs(count - 315672 / 3)
        if offset > max_offset:
            max_offset = offset
            print(offset, ":", all_count)
        count = 0
        all_count += 1
        if all_count % 10000 == 0:
            print(all_count)