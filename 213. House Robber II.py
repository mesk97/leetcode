# https://leetcode.com/problems/house-robber-ii/?envType=study-plan&id=algorithm-ii
# 213. House Robber II
# Medium
# 7.7K
# 114
# Companies
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 3:
# Input: nums = [1,2,3]
# Output: 3

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

# Checking 
#    build chain variate +2, +3 (+4 is not relevant -> +2 +2)
#    correctly check ends 
#    start from 0, 1, 2 (it is required because can produce option which is no include 0 and 1), 
#       3 (NO -> no option to don't include 1 in such case )
class Item:
    def __init__(self, index, prev, nums):
        self.index = index
        self.prev = prev

        if prev == None:
            self.first = index
            self.sum = 0
        else:
            self.first = prev.first
            self.sum = prev.sum
        
        self.sum += nums[index]
        pass

def is_last_and_first_are_near(item, index, nums):
    if index < (len(nums) - 1):
        return False
    # last is set, check first  
    if item.first == 0:
        return True
    return False

# optimization logic:
#   check that we already pass from first -> next .. and check sum
#   and continue processing only if sum is more or we don't pass 
def check_and_add_next_try(stack, next_index, item, nums):
    global processed

    pair = (item.first, next_index)
    if pair not in processed or processed[pair] < item.sum:
        processed[pair] = item.sum
        stack.append(Item(next_index, item, nums))

def main(nums):
    global processed
    processed = dict()

    stack = []
    result = 0

    if len(nums) > 0:
        stack.append(Item(0, None, nums))
    if len(nums) > 1:
        stack.append(Item(1, None, nums))
    if len(nums) > 2:
        stack.append(Item(2, None, nums))

    while len(stack) > 0:
        item = stack.pop()
        last = item.index

        if item.sum > result:
            result = item.sum

        # check case +2
        if (last + 2) < len(nums) and not is_last_and_first_are_near(item, last + 2, nums):
            check_and_add_next_try(stack, last + 2, item, nums)

        # check case +3
        if (last + 3) < len(nums) and not is_last_and_first_are_near(item, last + 3, nums):
            check_and_add_next_try(stack, last + 3, item, nums)

    return result

if __name__ == "__main__":
    nums = [1,2,3,1]
    nums = [2, 3, 2]
    nums = [200,3,140,20,10]

    # time limit
    nums = [114,117,207,117,235,82,90,67,143,146,53,108,200,91,80,223,58,170,
            110,236,81,90,222,160,165,195,187,199,114,235,197,187,69,129,64,214,
            228,78,188,67,205,94,205,169,241,202,144,240]

    print(main(nums))