# TWO pointers

# https://leetcode.com/problems/container-with-most-water/description/
# 11. Container With Most Water
# Medium
# Topics
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

def volume(heights, begin, end):
    if end < begin:
        return 0
    min = heights[begin]
    if heights[end] < min:
        min = heights[end]
    return min * (end - begin)

def find_bigger(heights, current, increment):
    ethalon = heights[current]
    while current >= 0 and current < len(heights):
        current = current + increment
        if heights[current] >= ethalon:
            return current
    return current

def main(heights):
    begin = 0
    end = len(heights) - 1
    result = 0
    
    while end > begin:
        new_volume = volume(heights, begin, end)
        if new_volume > result:
            result = new_volume

        # двигаем самый маленький -> растим стенку
        if heights[begin] < heights[end]:
            begin = find_bigger(heights, begin, 1)
        else:
            end = find_bigger(heights, end, -1)

    return result

if __name__ == "__main__":
    heights = [1, 8,6,2,5,4,8,3,7]
    #heights = [1,3,2,5,25,24,5]
    print(main(heights))