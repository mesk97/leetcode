# https://leetcode.com/problems/arithmetic-slices/?envType=study-plan&id=algorithm-ii

# 413. Arithmetic Slices
# Medium
# 4.8K
# 277
# Companies
# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.

# A subarray is a contiguous subsequence of the array.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

# Example 2:
# Input: nums = [1]
# Output: 0

# Constraints:

# 1 <= nums.length <= 5000
# -1000 <= nums[i] <= 1000

# logic:
# 1. находим длинные цепочки с одинаковым дифом
# 2. каждая цепочка с длинной N (кол-во одинаковых дифов) добавляет  (N-1)*N/2

def add_new_diff_range(range_lenght):
    return int(range_lenght * (range_lenght + 1) / 2)

def main(nums):
    result = 0
    
    last_diff = None
    range_lenght = 0
    
    for i in range(1, len(nums)):
        new_diff = nums[i] - nums[i-1]
        if last_diff is None or last_diff != new_diff:
            last_diff = new_diff
            result += add_new_diff_range(range_lenght)
            range_lenght = 0
            continue

        # last_diff == new_diff
        range_lenght += 1

    result += add_new_diff_range(range_lenght)
    return result

if __name__ == "__main__":
    # nums = [1, 2, 3, 4]
    nums = [1, 2, 3]
    print(main(nums))

