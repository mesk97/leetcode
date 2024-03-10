# https://leetcode.com/problems/reverse-nodes-in-k-group/
# 21.59
# 22^04
# 22.35 - дебаг первой версии - не полной 

# 25. Reverse Nodes in k-Group
# Hard
# Topics
# Companies
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
 

# Follow-up: Can you solve the problem in O(1) extra memory space?

# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Accepted
# 865.3K
# Submissions
# 1.5M
# Acceptance Rate
# 57.9%
# Topics
# Linked List
# Recursion

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def transform2ListNode(list):
    if len(list) == 0:
        return None
    result = ListNode(list[0])
    last = result
    for l in list[1:]:
        new = ListNode(l)
        last.next = new
        last = new

    return result

def transformFromListNode(list):
    result = []
    while list is not None:
        result.append(list.val)
        list = list.next
    return result

def find_block(first, k):
    i = 0
    while i < (k-1) and not first is None:
        i = i + 1
        first = first.next

    if first is None:
        return (None, None)

    return (first, first.next)

def change_order(first, last):
    current = first
    next = current.next
    while current != last:
        new_next = next.next
        next.next = current
        current = next 
        next = new_next

def main(head, k):
    if k == 1:
        return head 

    firstest = None
    last = None
    next = None
    first = head

    while not first is None:
        # 1.  находим что есть блок и его ключевые параметры 
        (new_first, new_next) = find_block(first, k)
        
        # 2. не хватает элементов на целый блок
        if new_first is None:
            break

        next = new_next

        # 3. начало первого повернутого блока
        if firstest is None:
            firstest = new_first

        # 4. последний элемент
        new_last = first

        # 5. меняем порядок в блоке
        change_order(new_last, new_first)

        # 6. перецепляем прошлый последний элемент
        if not last is None:
            last.next = new_first

        # 7. новый последний
        last = new_last

        # 8. начало нового блока
        first = next

    # Зацепляем концевик
    if not last is None:
        last.next = next
    return firstest

import unittest
class Test(unittest.TestCase):
    #setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.item_4 = ListNode(4)
        self.item_3 = ListNode(3, self.item_4)
        self.item_2 = ListNode(2, self.item_3)
        self.item_1 = ListNode(1, self.item_2)
        return

    def test_find_block_3(self):
        (new_first, new_next) = find_block(self.item_1, 3)
        self.assertEqual(new_first, self.item_3)
        self.assertEqual(new_next, self.item_4)

    def test_find_block_2(self):
        (new_first, new_next) = find_block(self.item_2, 2)
        self.assertEqual(new_first, self.item_3)
        self.assertEqual(new_next, self.item_4)

    def test_change_order_3_of_4(self):
         change_order(self.item_1, self.item_3)
         self.assertEqual(self.item_3.next, self.item_2)
         self.assertEqual(self.item_4.next, None)

    def test_change_order_4_of_4(self):
         change_order(self.item_1, self.item_4)
         self.assertEqual(self.item_3.next, self.item_2)
         self.assertEqual(self.item_4.next, self.item_3)

    def test_change_order_2_of_4(self):
         change_order(self.item_1, self.item_2)
         self.assertEqual(self.item_2.next, self.item_1)
         self.assertEqual(self.item_3.next, self.item_4)

if __name__ == "__main__":
    head = [1,2,3,4,5]
    k = 3
    print(transformFromListNode(main(transform2ListNode(head), k)))
    #unittest.main()