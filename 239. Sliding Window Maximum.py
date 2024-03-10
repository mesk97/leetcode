# https://leetcode.com/problems/sliding-window-maximum/description/

# 21^43
# 21.50 понятен алгоритм 
# 22^03 - закончили кодинг
# 22.13 - окончил локальную отладку 
# приняли с первого раза

# 239. Sliding Window Maximum
# Hard
# Topics
# Companies
# Hint
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length
# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Accepted
# 966.8K
# Submissions
# 2.1M
# Acceptance Rate
# 46.5%
# Topics
# Array
# Queue
# Sliding Window
# Heap (Priority Queue)
# Monotonic Queue

import collections

def remove_from_deq(deq, item):
    #print("remove", deq, item)
    if item == deq[0]:
        deq.popleft()
    return 

def add_to_deq(deq, item):
    #print("add", deq, item)
    
    ## сортированная очередь 
    # более старшие заменяют последние 
    # меньше и такие же - просто добавляются
    while len(deq) > 0 and deq[-1] < item:
        deq.pop()
    deq.append(item)
    return 

def main(nums, k):
    deq = collections.deque()

    # инитим первые 
    for i in range(0, k):
        add_to_deq(deq, nums[i])

    result = [ deq[0] ]

    pointer = k
    while pointer < len(nums):
        #print("result", result)
        remove_from_deq(deq, nums[pointer - k])
        add_to_deq(deq, nums[pointer])
        result.append(deq[0])
        pointer = pointer + 1

    return result

if __name__ == "__main__":
    n = 8
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(main(nums, k))
