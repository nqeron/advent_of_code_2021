def analyze(file):
    with open(file) as f:
        nums = [int(line.strip()) for line in f]
    total = 0
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            total += 1
    print(total)


if __name__ == '__main__':
    analyze("inputs/day01.txt")