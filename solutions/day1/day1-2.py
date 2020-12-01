import numpy as np
# 3 sum/triplet problem!
# like before, but find 3 numbers that sum to 2020 and return all three values multiplied together
# using same input

def find2020(nums):
    nums.sort() # sort to make life easy
    n = len(nums)
    for idx in range(0,n-1): #range doesn't include last value,so for our window to work correctly add 1 to n-2
        j = nums[idx]
        left, right = idx+1, n-1 #set search window
        while left < right:
            sum = nums[idx]+nums[left]+nums[right]

            if sum == 2020:
                answer = nums[idx]*nums[left]*nums[right]
                return (answer)
            elif sum < 2020:
                left += 1
            else: # sum > 2020
                right -= 1


if __name__ == '__main__':
    in_data = np.loadtxt('../data/day1/input-p1.txt')
    answer = find2020(in_data.tolist())
    print(int(answer))
