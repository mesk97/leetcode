# 221. Maximal Square
# Medium
# 9.6K
# 206
# Companies
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.


# Example 1:


# Input: matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
#     "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
# Output: 4
# Example 2:


# Input: matrix = [["0", "1"], ["1", "0"]]
# Output: 1
# Example 3:

# Input: matrix = [["0"]]
# Output: 0


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.

# Algo 
#   Идем из верхгнего левого угла 
#   если у ячейки ее левый, верхний и по диагонали это 1 и она сама 1 .. 
#   то ее мощность становится 1 + минимум мощи ее соседей,
#   т.е. если все соседи составляют квадратик 2х2 то она уже готова составить 3х3

def main(matrix):
    max = 0

    row = len(matrix)
    if row == 0:
        return 0
    column = len(matrix[0])

    for r in range(0, row):
        for c in range(0, column):
            matrix[r][c] = int(matrix[r][c])

    for r in range(0, row):
        for c in range(0, column):
            if r > 0 and c > 0 and matrix[r][c] > 0:
                matrix[r][c] = matrix[r][c] + min(matrix[r - 1][c - 1], 
                                                  matrix[r][c - 1], 
                                                  matrix[r - 1][c])
            if matrix[r][c] > max:
                max = matrix[r][c]

    return max*max

if __name__ == "__main__":
    # matrix = [["0", "1"], ["1", "0"]]
    # matrix = [["1", "0", "1", "0", "0"], 
    #           ["1", "0", "1", "1", "1"], 
    #           ["1", "1", "1", "1", "1"], 
    #           ["1", "0", "0", "1", "0"]]
    matrix = [["1", "0", "1", "1", "0", "1"],
              ["1", "1", "1", "1", "1", "1"],
              ["0", "1", "1", "0", "1", "1"],
              ["1", "1", "1", "0", "1", "0"],
              ["0", "1", "1", "1", "1", "1"],
              ["1", "1", "0", "1", "1", "1"]]
    print(main(matrix))
