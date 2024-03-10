# https://leetcode.com/problems/permutations-ii/?envType=study-plan&id=algorithm-ii

# 47. Permutations II
# Medium
# 6.9K
# 125
# Companies
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
# Constraints:
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

# Logic:
# 1. go through stack 
# 2. keep structure of item 
#         index in massive 
#         value
#         reference to prev value -> need for build chain 
#    3. for each item in stack 
#    4. put next items to stack 
#         pass from  index -> end of array
#         skip repeating items 
#         next item -> prev = item 

#     5. when index on end -> print array
#     get from top of stack -> to don't encrease stack numbers

class Item:
    def __init__(self, used, value, prev):
        self.used = used
        self.value = value
        self.prev = prev
        pass

def get_chain(item):
    result = []
    while item.value != None:
        result.append(item.value)
        item = item.prev
    return result

def main(_nums):
    nums = sorted(_nums)
    results = []
    stack = [ Item(set(), None, None) ]

    while len(stack) > 0:
        item = stack.pop()
        last = None
        for i in range(0, len(nums)):
            value = nums[i]
            if value == last:
                continue
            if i in item.used:
                continue

            last = value
            used = item.used.copy()
            used.add(i)
            stack.append(Item(used, value, item))
        
        # it was last element
        if last == None:
            results.append(get_chain(item))

    return results

if __name__ == "__main__":
    #nums = [1,2,3]
    nums = [1,1,2]
    print(main(nums))