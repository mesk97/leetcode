# https://leetcode.com/problems/longest-increasing-subsequence/description/

# 300. Longest Increasing Subsequence
# Medium
# Topics
# Companies
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
 

# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2.1M
# Submissions
# 3.6M
# Acceptance Rate
# 57.3%
# Topics
# Array
# Binary Search
# Dynamic Programming

# Algo 
# 1. имеем массив длин 
# 2. записываем максимальный в ряду для этой длины
# 3. для каждого нового эдемента начинаем с максимальной длины
# d[0] = -minimust
# 4. если  d[i] < item  то d[i+1] = max(item, d[i+1])
# 5. maxlen = max(maxlen, i+1)


# Runtime
# 13
# ms
# Beats
# 73.23%
# Analyze Complexity
# Memory
# 18.33
# MB
# Beats
# 10.31%


MINIMUST = -10*10*10*10-1
MAXLEN = 2500+1


def main(nums):
    maxlen = 1
    d = [None]*MAXLEN
    d[0] = MINIMUST
    d[1] = nums[0]

    for i in range(0, len(nums)):
        item = nums[i]

        # 3. для каждого нового эдемента начинаем с максимальной длины
        iterate = maxlen
        while iterate >= 0:
            # 4. если  d[i] < item  то d[i+1] = max(item, d[i+1])
            if d[iterate] < item:
                if d[iterate + 1] is None:
                    d[iterate + 1] = item
                else:
                    d[iterate + 1] = min(item, d[iterate + 1])
                # 5. maxlen = max(maxlen, i+1)
                maxlen = max(maxlen, iterate + 1)
                break
            iterate = iterate - 1

    return maxlen

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]

    print(main(nums))