# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# 13.13
# 13.25 придумал и записал алгоритм 
# 1. начинаем с краевых нод
# 2. дальше у каждой ноды проверяем
#       A 
#      / \
#     L   R
# 3.есть несколько моментов
#   1. либо пути L A R, L A, L R ->  сравниваем с максималкой
#   2. либо апдейтим в A path_max .. сравнивая  L A, A, R A
# 4. будем в стэк складывать ноды (не забыть ап ноду)
# 5. обрабатываем (чекаем и выкидываем из стэка) те у кого L=None или посечен L-path_max и для R так же
# 21.45 начинаю кодить 
# 22.07 закончил кодинг
# 22.09 fail 73 / 96 testcases passed
# 22.20 прошел но плохие результаты 
# Runtime
# 77
# ms
# Beats
# 16.62%
# of users with Python3
# Memory
# 22.72
# MB
# Beats
# 6.20%
# of users with Python3


# 124. Binary Tree Maximum Path Sum
# Hard
# Topics
# Companies
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:


# Input: root = [-10,9,20,None,None,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 3 * 104].
# -1000 <= Node.val <= 1000
# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Accepted
# 1.2M
# Submissions
# 2.9M
# Acceptance Rate
# 39.9%
# Topics
# Dynamic Programming
# Tree
# Depth-First Search
# Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def fromListToTreeNode(rootlist):
    if len(rootlist) == 0:
        return None
    root = TreeNode(rootlist.pop(0))
    stack = [root]
    while len(stack) > 0 and len(rootlist) > 0:
        tofill = stack.pop(0)
        left = rootlist.pop(0)
        right = rootlist.pop(0)
        if not left is None:
            item = TreeNode(left)
            tofill.left = item
            stack.append(item)
        if not right is None:
            item = TreeNode(right)
            tofill.right = item
            stack.append(item)
    return root

# 1. начинаем с краевых нод
# 2. дальше у каждой ноды проверяем
#       A 
#      / \
#     L   R
# 3.есть несколько моментов
#   1. либо пути L A R, L A, A R ->  сравниваем с максималкой
#   2. либо апдейтим в A path_max .. сравнивая  L A, A, R A
# 4. будем в стэк складывать ноды (не забыть ап ноду)
# 5. обрабатываем (чекаем и выкидываем из стэка) те у кого L=None или посечен L-path_max и для R так же

def isFinal(item, pathMax):
    return item in pathMax

def updateAndGetMaxPath(item, pathMax):
    path_a = item.val
    path_l_a = item.val + pathMax[item.left]
    path_a_r = item.val + pathMax[item.right]
    path_l_a_r = pathMax[item.left] + item.val + pathMax[item.right]

    maximum_to_set = max(path_a, path_l_a, path_a_r)
    pathMax[item] = maximum_to_set
    return max(maximum_to_set, path_l_a_r)

def main(rootNode):
    pathMax = dict()
    pathMax[None] = 0

    stack = [ rootNode ]
    result = None
    
    while len(stack) > 0:
        item = stack.pop()
        if isFinal(item.left, pathMax) and isFinal(item.right, pathMax):
            new_result = updateAndGetMaxPath(item, pathMax)
            if result is None or new_result > result:
                result = new_result
            continue

        stack.append(item)
        if not isFinal(item.left, pathMax):
            stack.append(item.left)
        if not isFinal(item.right, pathMax):
            stack.append(item.right)

    return result

if __name__ == "__main__":
    #root = [1,2,3]
    root = [5,4,8,11,None,13,4,7,2,None,None,None,1] # expected 48

    print(main(fromListToTreeNode(root)))
    #unittest.main()