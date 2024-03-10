
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/?envType=study-plan&id=algorithm-ii
# 153. Find Minimum in Rotated Sorted Array
# Medium
# 9.3K
# 446
# Companies
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

def main(nums):
    begin_index = 0
    end_index = len(nums)-1
    if (nums[begin_index] < nums[end_index]):
        return nums[begin_index]    
    while begin_index < end_index-1:
        middle = int((end_index + begin_index)/2)
        if nums[middle] >= nums[begin_index]:
            begin_index = middle
        else:
            end_index = middle
    if (nums[begin_index] < nums[end_index]):
        return nums[begin_index]    
    return nums[end_index]

if __name__ == "__main__":
    #nums = [3,4,5,6,1,2]
    nums = [11,13,15,17]
    print(main(nums))