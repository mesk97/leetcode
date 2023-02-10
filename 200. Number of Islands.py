# https://leetcode.com/problems/number-of-islands/submissions/869088356/?envType=study-plan&id=algorithm-ii
# 200. Number of Islands
# Medium
# 18.4K
# 408
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

def color_it(color, i, j, value, grid, num_lines, num_columns, stack):
    if value == 0 or value == color:
        return
    if value > 1:
        print("BUG!!")
        exit(1)
    
    #print(color, i, j, value)

    # value == 1
    grid[i][j] = color

    # color all neighbours
    if i > 0:
        stack.append((i-1, j))
    if j > 0:
        stack.append((i, j-1))  
    if i < (num_lines-1):
        stack.append((i+1, j))
    if j < (num_columns-1):
        stack.append((i, j+1))

def main(grid):
    # go through grid 
    # if find "1" -> starting coloring in all direction (with put to stack)
    color = 1
    num_lines = len(grid)
    num_columns = 0
    if num_lines > 0:
        num_columns = len(grid[0])

    for (i, raw_of_grid) in enumerate(grid):
        for (j, value) in enumerate(raw_of_grid):
            #print (i, j, value)
            value = int(value)
            #continue
            if value == 1:
                color += 1
                #print (color)
                stack = [(i, j)]
                while len(stack) > 0:
                    (si, sj) = stack[0]
                    color_it(color, si, sj, int(grid[si][sj]), grid, num_lines, num_columns, stack)
                    del stack[0]
    return color-1

if __name__ == "__main__":
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print (main(grid))