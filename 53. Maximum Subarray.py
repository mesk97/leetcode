# https://leetcode.com/problems/maximum-subarray/description/

# 53. Maximum Subarray
# Medium
# Topics
# Companies
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 4.1M
# Submissions
# 8M
# Acceptance Rate
# 51.0%
# Topics
# Array
# Divide and Conquer
# Dynamic Programming

# алго
# идея как решать пришла после того как нарисовал на бумаге
# по сути находим минимум суммы начиная с начала и находим максимум суммы начиная с начала 
# и вот разница между этими двумя точками и будет тот наш максимальный подмассив
#         /\
#      /\/  \           
#     /      \
# \  /
#  \/

# Wrong Answer
# 126 / 210 testcases passed

# Editorial
# Input
# nums =
# [-1]

# Wrong Answer
# 117 / 210 testcases passed

# Editorial
# Input
# nums =
# [-2,1]

# Use Testcase
# Output
# 0
# Expected
# 1
# решение норм работает когда минимумы и максимумы не на краях

MAXIMUM_NUMBER = 10*10*10*10+1
MINIMUM_NUMER = -MAXIMUM_NUMBER

def main(nums):
#    minimum = MAXIMUM_NUMBER
#    maximum = MINIMUM_NUMER
    minimum = 0
    maximum = nums[0]
    result = maximum - minimum

    for n in nums[1:]:
        result = result + n
        minimum = min(minimum, result)
        maximum = max(maximum, result)

    return maximum - minimum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    #nums = [1]
    #nums = [-1]
    nums = [-2, 1]

    print(main(nums))