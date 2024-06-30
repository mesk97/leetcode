# https://leetcode.com/problems/unique-paths/description/

# 62. Unique Paths
# Attempted
# Medium
# Topics
# Companies
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
 

# Constraints:

# 1 <= m, n <= 100
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.9M
# Submissions
# 2.9M
# Acceptance Rate
# 64.5%
# Topics
# Math
# Dynamic Programming
# Combinatorics

def main(m, n):
    result = 0

    # преалоцируем
    d = [[0] * (n + 1)] * (m + 1)

    # предзаполним края чтобы не смотреть за выход за границы
    # for i in range(0, m + 1):
    #     d[i][0] = 0
    # for j in range(0, n + 1):
    #     d[0][j] = 0

    # зайдем с одного сбоку
    d[0][1] = 1

    for i in range(1, m + 1):
        for j in range (1, n + 1):
            d[i][j] = d[i-1][j] + d[i][j-1]

    return d[m][n]

if __name__ == "__main__":
    m = 3
    n = 7
    print(main(m, n))