# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=study-plan&id=algorithm-ii
# 34. Find First and Last Position of Element in Sorted Array
# Medium
# 15.2K
# 363
# Companies
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

def find_first_entry(nums, target):
    begin_index = 0
    end_index = len(nums) - 1

    while ((end_index - begin_index) >= 2):
        middle = int((end_index + begin_index)/2)
        if nums[middle] < target:
            begin_index = middle
        else:
            end_index = middle

    if nums[begin_index] == target:
        return begin_index
    elif nums[end_index] == target:
        return end_index
    return None

def find_last_entry(nums, target):
    begin_index = 0
    end_index = len(nums) - 1

    while ((end_index - begin_index) >= 2):
        middle = int((end_index + begin_index)/2)
        if nums[middle] > target:
            end_index = middle
        else:
            begin_index = middle

    if nums[end_index] == target:
        return end_index
    elif nums[begin_index] == target:
        return begin_index
    return None


def main(nums, target):    
    return [find_first_entry(nums, target), find_last_entry(nums, target)]

if __name__ == "__main__":
    nums = [5,6,7,8,8,8,10]
    target = 8
    print (main(nums, target))