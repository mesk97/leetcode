# https://leetcode.com/problems/minimum-path-sum/description/

# 64. Minimum Path Sum
# Medium
# Topics
# Companies
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

 

# Example 1:


# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.2M
# Submissions
# 1.9M
# Acceptance Rate
# 64.3%
# Topics
# Array
# Dynamic Programming
# Matrix

# алго как Unique path 2 +
# сравниваем верх и низ 

MAXIMUM = 10000
def main(grid):

    m = len(grid)
    n = len(grid[0])

    # преалоцируем - !!!! ниже неверный способ - там одинаковые указатели ! факк 
    # d = [[0] * (n + 1)] * (m + 1)
    d = [[0] * (n + 1) for i in range(m + 1)]

    # предзаполним края чтобы не смотреть за выход за границы
    for i in range(0, m + 1):
        d[i][0] = MAXIMUM
    for j in range(0, n + 1):
        d[0][j] = MAXIMUM

    # зайдем с одного боку
    d[0][1] = 0

    for i in range(1, m + 1):
        for j in range (1, n + 1):
            minimum = d[i-1][j]
            if d[i][j-1] < minimum:
                minimum = d[i][j-1]
            d[i][j] = minimum + grid[i-1][j-1] 

    return d[m][n]

if __name__ == "__main__":
    grid = [
            [1,3,1],
            [1,5,1],
            [4,2,1]]
    print(main(grid))