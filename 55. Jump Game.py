# https://leetcode.com/problems/jump-game/?envType=study-plan&id=algorithm-ii

# 55. Jump Game
# Medium
# 15.3K
# 784
# Companies
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

# Logic 
#   attempts in stack
#   try different options 
#   optimize if you already was on this step 
class Item:
    def __init__(self, index):
        self.index = index
        pass

def main(nums):
    stack = []
    processed = set()

    stack.append(Item(0))
    while len(stack) > 0:
        item = stack.pop()
        position = item.index

        for i in range(0, nums[position] + 1):
            new_position = position + i
            if new_position == (len(nums) - 1):
                return True

            if new_position not in processed:
                processed.add(new_position)
                stack.append(Item(new_position))          

    return False

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    #nums = [2,0,1,1,4]
    #nums = [3,2,1,0,4]
    print(main(nums))