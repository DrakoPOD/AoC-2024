def main():
    data = []
    disk = []

    with open('./data_day09.txt') as f:
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

    for i in range(0, len(disk)):
        reverse_i = len(disk) - i - 1
        last_block = disk[reverse_i]

        if last_block == '.':
            continue
        else:
            for ii in range(len(disk)):
                if disk[ii] == '.':
                    disk[ii] = last_block
                    disk[reverse_i] = '.'
                    break

            defragmented = True
            for ii in range(reverse_i):
                if disk[ii] == '.':
                    defragmented = False
                    break
            
            if defragmented:
                break

    checksum = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            continue
        checksum += disk[i] * i

    print(checksum)

if __name__ == '__main__':
    main()