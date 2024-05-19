# https://leetcode.com/problems/surrounded-regions/description/
# 130. Surrounded Regions
# Medium
# Topics
# Companies
# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

# Example 1:


# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
# Example 2:

# Input: board = [["X"]]
# Output: [["X"]]
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 689.1K
# Submissions
# 1.8M
# Acceptance Rate
# 39.3%
# Topics
# Array
# Depth-First Search
# Breadth-First Search
# Union Find
# Matrix

class Island:
    def __init__(self, row, col):
        # 0 - alone island
        # 1 - border island
        self.state = 0
        self.coordinates = set()
        self.coordinates.add((row, col))

    def setBorder(self):
        self.state = 1

    def join(self, other_island):
        # перенести стэйт
        ТУДУ 

        # впитать 
        ТУДу

        # поменять на новый island 
        for (row, col) in other_island.coordinates:
            board[row][col] = self

        # убрать из списка островов
        set(islandsSet).remove(other_island)

        

def check(board, row_tocheck, col_tocheck, row, col):
    island = board[row][col]

    # если граница ?
    if row_tocheck < 0 or col_tocheck < 0 or row_tocheck == rows_num or col_tocheck == cols_num:
        island.setBorder()
        return
    
    # если море или не размеченный остров
    if board[row_tocheck][col_tocheck] == 'X' or board[row_tocheck][col_tocheck] == 'O':
        return

    # если помеченый остров
    other_island = board[row_tocheck][col_tocheck]
    other_island.join(island)


def main(board):
    rows_num = len(board)
    cols_num = len(board[0])
    islandsSet = set()

    for row in range(0, rows_num):
        for col in range(0, cols_num):
            point = board[row][col]
            if point == 'X':
                continue
            # point == 'O'
            isl = Island(row, col)
            islandsSet.add(isl)
            board[row][col] = isl


            check(board, row-1, col)
            check(board, row+1, col)
            check(board, row, col-1)
            check(board, row, col+1)

    # пройти по всем островам и покрасить плохие
    ТУДУ

    return board

if __name__ == "__main__":
    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]]
    #Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

    print(main(board))