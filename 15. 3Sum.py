# https://leetcode.com/problems/3sum/?envType=study-plan&id=algorithm-ii
# 15. 3Sum
# Medium
# 23K
# 2.1K
# Companies
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

def find_sum(sum, nums):
    print(sum, nums)
    found = []
    begin = 0
    end = len(nums) - 1
    while begin < end:
        result = sum + nums[begin] + nums[end]
        if result > 0:
            end = end - 1
        elif result < 0:
            begin = begin + 1
        else:
            found.append([sum, nums[begin], nums[end]])
            begin = begin + 1
    return found

# sorted array
# fixate 1 number 
# try find sum with two pointers technik
#   is sum > value ... decrease right pointer .. otherwise left 
def main(_nums):
    results = []
    nums = sorted(_nums)
    if len(nums) < 3:
        return []
    print(nums)
    last_sum = None
    for i in range(0, len(nums)-2):
        sum = nums[i]
        if sum == last_sum:
            continue
        last_sum = sum
        rbulk = find_sum(sum, nums[i+1:len(nums)])
        for r in rbulk:
            #results.append(r)
            if len(results) == 0:
                results.append(r)
            else:
                last = results[-1]
                if not(last[0] == r[0] and last[1] == r[1] and  last[2] == r[2]):
                    results.append(r)
            
    return results

if __name__ == "__main__":
    #nums = [-1,0,1,2,-1,-4]
    #nums = [-5, 1, 2, 3, 4]
    #nums = [0,0,0,0]
    #nums = [-2, -2, -1, -1, 0, 0, 1, 1]
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    print(main(nums))