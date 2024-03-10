# https://leetcode.com/problems/search-a-2d-matrix/?envType=study-plan&id=algorithm-ii
# 74. Search a 2D Matrix
# Medium
# 10.9K
# 323
# Companies
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

def main(matrix, target):
    last_raw = 0
    for i in range(0, len(matrix)):
        if matrix[i][0] > target:
            return target in matrix[last_raw]
        last_raw = i
    return target in matrix[last_raw]

if __name__ == "__main__":
    matrix = [[1]]
    target = 1
    print(main(matrix, target))