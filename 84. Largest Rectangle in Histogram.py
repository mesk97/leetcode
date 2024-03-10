# Stack
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
# 84. Largest Rectangle in Histogram
# Hard
# Topics
# Companies
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4
 

# Constraints:

# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104

# 22:19
# 22:52 - первая версия фэйл
# 19:15 - вторая попытка 
# 19^35

def main(heights):
    result = 0

    # хранит прямоуголники H, начальная точка X
    stack = [(0, -1)] # первый элемент чтобы не отрабатывать краевых случаев

    heights.append(0) # для финального вытеснения всех

    for x in range(0, len(heights)):
        h = heights[x]

        # проходим по стэку и вытесняем все элементы который выше
        out_x = x
        while True:        
            (last_h, last_x) = stack[-1] # последний элемент

            if h >= last_h:
                break

            # вытеснение
            if last_h * (x - last_x) > result:
                result = last_h * (x - last_x)
            out_x = last_x
            stack.pop()

        stack.append((h, out_x))

    return result

if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    heights = [3,6,5,7,4,8,1,0]
    print(main(heights))