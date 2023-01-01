# https://leetcode.com/problems/search-in-rotated-sorted-array/?envType=study-plan&id=algorithm-ii
# 33. Search in Rotated Sorted Array
# Medium
# 19.1K
# 1.1K
# Companies
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

def search(nums, begin_index, end_index, target):
    while ((end_index - begin_index) >= 2):
        middle = int((end_index + begin_index)/2)

        if nums[begin_index] < nums[end_index]:
            if nums[middle] >= target:
                end_index = middle
            else:
                begin_index = middle
            continue
    
    if nums[begin_index] == target:
        return begin_index
    if nums[end_index] == target:
        return end_index
    return -1

def find_top(nums):
    begin_index = 0
    end_index = len(nums) - 1

    while ((end_index - begin_index) >= 2):
        middle = int((end_index + begin_index)/2)
        if nums[middle] < nums[begin_index]:
            end_index = middle
        else:
            begin_index = middle
    
    if nums[begin_index] > nums[end_index]:
        return begin_index
    return end_index

def main(nums, target):
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        if nums[0] == target:
            return target
        return -1

    top = find_top(nums)
    if target <= nums[top] and target >= nums[0]:
        return search(nums, 0, top, target)

    if top == (len(nums) - 1):
        return -1
    return search(nums, top+1, len(nums)-1, target)

if __name__ == "__main__":
    nums = [4,5,6,7,8,1,2,3]

    target = 5
    print (main(nums, target))