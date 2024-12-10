def __main__():
    operations = []

    with open('./data_day07.txt', 'r') as f:
        for line in f:
            result, nums = line.strip().split(': ')
            result = int(result)
            nums = list(map(int,nums.split(' ')))
            operations.append([result,nums])

    def operate_and_concat(i, total, nums, counts):
        for operator in ['+','*','||'] :
            total2 = total
            if operator == '+':
                total2 = total + nums[i]
            elif operator == '*':
                total2 = total * nums[i]
            elif operator == '||':
                total2 = int(str(total) + str(nums[i]))

            if i < len(nums)-1:
                operate_and_concat(i+1, total2, nums, counts)
            else:
                counts.append(total2)

    count = []

    for operation in operations:
        num, nums = operation 
        counts = []
        operate_and_concat(1, nums[0], nums, counts)

        if num in counts:
            count.append(num)

    print(sum(count))

if __name__ == '__main__':
    __main__()