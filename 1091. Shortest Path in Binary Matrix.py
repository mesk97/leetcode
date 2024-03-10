# https://leetcode.com/problems/shortest-path-in-binary-matrix/?envType=study-plan&id=algorithm-ii
# 1091. Shortest Path in Binary Matrix
# Medium
# 4.3K
# 177
# Companies
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

# Example 1:
# Input: grid = [[0,1],[1,0]]
# Output: 2

# Example 2:
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

# Example 3:
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
 
# Constraints:
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1

def main(grid):
    # go through grid[0][0] 
    # check and mark all 0 -> put to value current step if value in grid is less
    # put to stack
    num_of_lines = len(grid)
    if num_of_lines == 0:
        return -1
    num_of_columns = len(grid[0])
    
    stack = [(0, 0, 2)]
    while len(stack) > 0:
        (y, x, color) = stack[0]
        del stack[0]

        if grid[y][x] != 0:
            continue  

        if y == (num_of_lines - 1) and x == (num_of_columns - 1):
            return color - 1

        grid[y][x] = color
        if y > 0:  # up
            stack.append((y-1, x, color+1))
        if x > 0:  # left
            stack.append((y, x-1, color+1))
        if y < (num_of_lines - 1): # below
            stack.append((y+1, x, color+1))
        if x < (num_of_columns - 1): # right
            stack.append((y, x+1, color+1))

        # diagonals
        if y > 0 and x > 0: # up + left
            stack.append((y-1, x-1, color+1))
        if y > 0 and x < (num_of_columns - 1): # up + right
            stack.append((y-1, x+1, color+1))
        if y < (num_of_lines - 1) and x > 0: # below + left
            stack.append((y+1, x-1, color+1))
        if y < (num_of_lines - 1) and x < (num_of_columns - 1): # below + right
            stack.append((y+1, x+1, color+1))

    return -1

if __name__ == "__main__":
    #grid = [[0,0,0],[1,1,0],[1,1,0]]
    grid = [[0,1],[1,0]]
    print (main(grid))