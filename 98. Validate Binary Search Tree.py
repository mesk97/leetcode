# 21.50
# 21.52 - понятно решение 
# 22.12 закодил
# 22.18 тест - нашел ошибку 
# 22.20  77 / 85 testcases passed
# 22.22 - осознал что не до конца верно осознал что такое BST 
# 22.39 - v2 с фиксом алгоритма
# 22.42 - фэйл 64 / 85 testcases passed
# 22.51 - дебагом - использовал кондишен дебаг - все таки дирекшен ... или мин макс нужен :)
# 12.40-12.56 - переделал логику  на UpLeft UpRight
# фэйл 82 / 85 testcases passed
# блин не учитывается кейз upLeft/upright через несколько уровней 
# 13.07 поправил и закончил


# 1. заполняем дерево -> можно кстати объединить заполнение и работу
# 2. имеем стэк
# 3. вытаскиваем по одному из стэка 
# 4. проверяем ноду из стэка 
# 5. если норм и листы не нулл кладем в стэк
# https://leetcode.com/problems/validate-binary-search-tree/description/
# 98. Validate Binary Search Tree
# Medium
# Topics
# Companies
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1
# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Accepted
# 2.2M
# Submissions
# 6.8M
# Acceptance Rate
# 32.7%
# Topics
# Tree
# Depth-First Search
# Binary Search Tree
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

def isCorrectTreeNode(item, upLeft, upRight):
    # структура проверки 
    #            UpLeft
    #                  \   
    #                    \ 
    #                   UpRight  - UpLeft or/and UpRight могут быть None - значит не проверяются
    #                     /
    #                    /
    #                Node
    #              /      \
    #            Left     Right      - Left or/and Right могут быть None - значит не проверяются 
    #     UpLeft < Left < Node < Right < UpRight

    if not item.left is None:
        if not (item.left.val < item.val):
            return False
        if not (upLeft is None or upLeft < item.left.val):
            return False 

    if not item.right is None:
        if not (item.right.val > item.val):
            return False
        if not (upRight is None or upRight > item.right.val):
            return False 

    return True

def main(rootNode):
    stack = [ (rootNode, None, None) ]
    while len(stack) > 0:
        (item, upLeft, upRight) = stack.pop(0)
        if not isCorrectTreeNode(item, upLeft, upRight):
            return False
        if not (item.left is None):
            stack.append((item.left, upLeft, item.val))  
        if not (item.right is None):
            stack.append((item.right, item.val, upRight)) 
    return True

import unittest
class Test(unittest.TestCase):
    #setUp method is overridden from the parent class TestCase
    def setUp(self):
        return

    def test_1size(self):
        root = fromListToTreeNode([1])
        self.assertEqual(root.val, 1)

    def test_3size(self):
        root = fromListToTreeNode([1, 2, 3])
        self.assertEqual(root.left.val, 2)

if __name__ == "__main__":
    root = [5,1,4,None,None,3,6]
    #root = [5,1,6]
    #root = [5,4,6,None,None,3,7]
    #root = [3,1,5,0,2,4,6]
    root = [120,70,140,50,100,130,160,20,55,75,110,119,135,150,200] # expected = false

    print(main(fromListToTreeNode(root)))
    #unittest.main()
