# https://leetcode.com/problems/unique-paths-ii/description/

# 63. Unique Paths II
# Medium
# Topics
# Companies
# Hint
# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# Example 2:


# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
 

# Constraints:

# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 965.1K
# Submissions
# 2.3M
# Acceptance Rate
# 41.9%
# Topics
# Array
# Dynamic Programming
# Matrix

# алго
# делаем как unic path 1
# d[i][j] равняется сумме только если в этом месте нет камня если камень то 0

def main(obstacleGrid):

    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    # преалоцируем
    d = [[0] * (n + 1)] * (m + 1)

    # зайдем с одного сбоку
    d[0][1] = 1

    for i in range(1, m + 1):
        for j in range (1, n + 1):
            if obstacleGrid[i-1][j-1] == 1:
                d[i][j] = 0
                continue
            d[i][j] = d[i-1][j] + d[i][j-1]

    return d[m][n]

if __name__ == "__main__":
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print(main(obstacleGrid))