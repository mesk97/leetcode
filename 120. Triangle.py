# https://leetcode.com/problems/triangle/description/

# 120. Triangle
# Medium
# Topics
# Companies
# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

# Example 1:

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:

# Input: triangle = [[-10]]
# Output: -10
 

# Constraints:

# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104
 

# Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 801.6K
# Submissions
# 1.4M
# Acceptance Rate
# 57.3%
# Topics
# Array
# Dynamic Programming

# определеяем изсходя из максимального возможного пути
MAXIMUM = 200*10*10*10*10+1
def main(triangle):
    V = len(triangle)
    H = V

    # преалоцируем - !!!! ниже неверный способ - там одинаковые указатели ! факк 
    # d = [[0] * (n + 1)] * (m + 1)
    # одновременно заполняем края чтобы их не обрабатывать 
    D = [[ MAXIMUM ] * (V + 1) for i in range(H + 1)]
    D[1][1] = triangle[0][0]

    for y in range(2, V+1):
        for x in range (1, y+1):
            D[y][x] = min(D[y-1][x-1],D[y-1][x]) + triangle[y-1][x-1]
            
    # минимум из последнего ряда
    return min(D[V])

if __name__ == "__main__":
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(main(triangle))
