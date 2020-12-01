import numpy as np
# 2 sum problem!
# find 2 values that equal a target (2020 in this case) given an array of numbers
# then return those two values multipled together

def find2020(nums):
    seen = {}
    for index, num in enumerate(nums):
        n1 = 2020 - num
        if n1 in seen:
            return [seen[n1], index]
        else:
            seen[num] = index
if __name__ == '__main__':
    in_data = np.loadtxt('data/day1/input-p1.txt')
    n1,n2 = find2020(in_data.tolist())
    print(int(in_data[n1]*in_data[n2]))
