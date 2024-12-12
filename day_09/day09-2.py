data = []
disk = []

with open('./example_day09.txt') as f:
    for line in f:
        data = (list(int(x) for x in line.strip()))

index = 0
for i, block in enumerate(data):
    if i % 2 == 0:
        for _ in range(block):
            disk.append(index)
        index += 1
    else:
        for _ in range(block):
            disk.append('.')
disk_2 = disk.copy()

disk2 = disk_2.copy()
i = 0
for _ in range(0, len(disk2)):
    reverse_i = len(disk2) - i - 1
    last_block = disk2[reverse_i]

    if last_block == '.':
        i += 1
        continue

    files = 1
    while True:
        if disk2[reverse_i - 1] == last_block:
            files += 1
            reverse_i -= 1
            i += 1
        else:
            i += 1
            break
    
    ii = 0
    located = False
    for _ in range(reverse_i - 1):
        free_space = 0
        if ii >= reverse_i:
            break
        if disk2[ii] == '.':
            found_at = ii
            free_space += 1
            while True:
                ii += 1
                if disk2[ii] == '.':
                    free_space += 1
                else:
                    break
            if free_space >= files:
                located = True
                for f in range(files):
                    disk2[found_at + f] = last_block
                    disk2[reverse_i + f] = '.'
        else:
            ii += 1

        if located:
            break
            

    if reverse_i == 0:
        break

print(disk2)