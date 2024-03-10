# 22.05 Начали
# 22.53 тяжко мержить - еще и List node

# https://leetcode.com/problems/merge-k-sorted-lists/description/

# 23. Merge k Sorted Lists
# Hard
# Topics
# Companies
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.
# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Accepted
# 1.9M
# Submissions
# 3.6M
# Acceptance Rate
# 52.0%
# Topics
# Linked List
# Divide and Conquer
# Heap (Priority Queue)
# Merge Sort

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        return main(lists)

def mergeListNode(q1, q2):
    result = None
    last = None
    # p1 = q1
    # p2 = q2
    # len1 = len(q1)
    # len2 = len(q2)

    while not q1 is None and not q2 is None:
        if q1.val < q2.val:
            item = ListNode(q1.val)
            q1 = q1.next
        else:
            item = ListNode(q2.val)
            q2 = q2.next
        if result is None:
            result = item
        else:
            last.next = item
        last = item
    
    # Добиваем концовку 
    if not q1 is None:
        if result is None:
            result = q1
        else:
            result.next = q1
    if not q2 is None:
        if result is None:
            result = q2
        else:
            result.next = q2
    return result

def merge(q1, q2):
    result = []
    p1 = 0
    p2 = 0
    len1 = len(q1)
    len2 = len(q2)

    while p1 < len1 and p2 < len2:
        if q1[p1] < q2[p2]:
            result.append(q1[p1])
            p1 = p1 + 1
        else:
            result.append(q2[p2])
            p2 = p2 + 1
    
    # добиваем концовку 
    if p1 < len1:
        result.extend(q1[p1:])
    if p2 < len2:
        result.extend(q2[p2:])

    return result


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

def transform(lists):
    result = []
    for list in lists:
        result.append(transform2ListNode(list))
    return result

def transformFromListNode(list):
    result = []
    while list is not None:
        result.append(list.val)
        list = list.next
    return result

import collections 
def main(lists):
    deq = collections.deque()
    #result = []
    for list in lists:
        deq.append(transformFromListNode(list))
    
    while len(deq) > 1:
        result = merge(deq.pop(), deq.pop())
        deq.appendleft(result)
        #result = merge(result, transformFromListNode(list))
    return transform2ListNode(deq.pop())



import unittest
class Test(unittest.TestCase):
    #setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.item_3 = ListNode(3)
        self.item_2_3 = ListNode(2, self.item_3)
        self.item_1_2_3 = ListNode(1, self.item_2_3)
        self.item_2_4_5 = ListNode(2, ListNode(4, ListNode(5)))

    def test_transform2ListNode(self):
        item = transform2ListNode([1, 2])
        self.assertEqual(item.next.val, 2)

    def test_transformFromListNode(self):
        result = transformFromListNode(self.item_2_4_5)
        self.assertSequenceEqual(result, [2, 4, 5])

    def test_merge_equal(self):
        result = merge(transformFromListNode(self.item_1_2_3), transformFromListNode(self.item_2_4_5))
        self.assertSequenceEqual(result, [1, 2, 2, 3, 4, 5])

    def test_merge_2_3(self):
        result = merge(transformFromListNode(self.item_2_3), transformFromListNode(self.item_2_4_5))
        self.assertSequenceEqual(result, [2, 2, 3, 4, 5])

    def test_merge_3_1(self):
        result = merge(transformFromListNode(self.item_2_4_5), transformFromListNode(self.item_3))
        self.assertSequenceEqual(result, [2, 3, 4, 5])

    # def test_mergeListNode(self):
    #     result = mergeListNode(self.item_1_2_3, self.item_2_4_5)
    #     self.assertSequenceEqual(transformFromListNode(result), [1, 2, 2, 3, 4, 5])
    

def main_test():
    unittest.main()

if __name__ == "__main__":
    lists = [[1,4,5],[1,3,4],[2,6]]
    print(transformFromListNode(main(transform(lists))))
    #main_test()