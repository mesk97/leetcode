# https://leetcode.com/problems/lru-cache/description/

# 21^50 начал 
# 22.07 понял алго ... дикт и линкедлист
# 22.33 -> 23.19 -> начали дебаг
# пробовал Unittest-ы на логику doublelinked -> реально рабочая тема - удалось найти ошибки 
# 1 submit -> 12 / 22 testcases passed


# 146. LRU Cache
# Medium
# Topics
# Companies
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.
# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Accepted
# 1.5M
# Submissions
# 3.7M
# Acceptance Rate
# 42.1%
# Topics
# Hash Table
# Linked List
# Design
# Doubly-Linked List

class DoubleLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.first_item = None
        self.last_item = None
        self.size = 0

    def len(self):
        return self.size

    def first(self):
        return self.first_item

    def remove(self, item):
        prev = item.prev
        next = item.next

        if prev is None:
            # это первый элемент
            self.first_item = next
        else:
            prev.next = next

        if next is None:
            # это последний элемент
            self.last_item = prev
        else:
            next.prev = prev
        
        item.prev = None
        item.next = None
        self.size = self.size - 1
        return
    
    def append(self, item):
        self.size = self.size + 1
        if self.first_item is None:
            self.first_item = item
            self.last_item = item
            return
        
        self.last_item.next = item
        item.prev = self.last_item
        self.last_item = item
        return


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = dict()
        self.order = DoubleLinkedList()

    def update_cache(self, item):
        #print("update_cache", item.key, item.value)
        self.order.remove(item)
        self.order.append(item)

    def get(self, key: int) -> int:
        if not key in self.values:
            #print("get not found", key)
            return -1
        item = self.values[key]
        self.update_cache(item)
        #print("get", key, item.value)
        return item.value

    def clear_last(self):

        to_delete = self.order.first()
        self.order.remove(to_delete)
        #print("clear_last ", to_delete.key, self.values)

        del self.values[to_delete.key]
        #print("clear_last_2", to_delete.key)


    def put(self, key: int, value: int) -> None:
        #print("put", key, value)

        if not key in self.values:
            item = DoubleLinkedListNode(key, value)
            self.values[key] = item
            if self.order.len() == self.capacity:
                self.clear_last()
            self.order.append(item)
        else:
            item = self.values[key]
            item.value = value # value могут апдейтнуть
            self.update_cache(item)
        return

def main(ops, values):
    result = []
    
    ops.pop(0)
    cache = LRUCache(values.pop(0)[0])

    while len(ops) > 0:
        op = ops.pop(0)
        val = values.pop(0)
        if op == "put":
            cache.put(val[0], val[1])
            result.append(None)
        else:
            result.append(cache.get(val[0]))

    return result

import unittest
class TestCalculator(unittest.TestCase):
    #setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.linked = DoubleLinkedList()
        self.item_1 = DoubleLinkedListNode(1, 11)
        self.item_2 = DoubleLinkedListNode(2, 22)
        self.item_3 = DoubleLinkedListNode(3, 33)
        self.item_4 = DoubleLinkedListNode(4, 44)

    def test_add_one(self):
        self.linked.append(self.item_1)
        self.assertEqual(self.linked.size, 1)
        self.assertEqual(self.linked.first_item, self.item_1)
        self.assertEqual(self.linked.last_item, self.item_1)

    def test_add_2_items(self):
        self.linked.append(self.item_1)
        self.linked.append(self.item_2)
        self.assertEqual(self.linked.size, 2)
        self.assertEqual(self.linked.first_item, self.item_1)
        self.assertEqual(self.linked.last_item, self.item_2)
        self.assertEqual(self.linked.last_item.prev, self.item_1)
        self.assertEqual(self.linked.first_item.next, self.item_2)

    def test_add_2_items_and_remove_first(self):
        self.linked.append(self.item_1)
        self.linked.append(self.item_2)
        self.linked.remove(self.item_1)
        self.assertEqual(self.linked.size, 1)
        self.assertEqual(self.linked.first_item, self.item_2)
        self.assertEqual(self.linked.last_item, self.item_2)

    def test_add_2_items_and_remove_last(self):
        self.linked.append(self.item_1)
        self.linked.append(self.item_2)
        self.linked.remove(self.item_2)
        self.assertEqual(self.linked.size, 1)
        self.assertEqual(self.linked.first_item, self.item_1)
        self.assertEqual(self.linked.last_item, self.item_1)

    def test_add_3_items_and_remove_middle(self):
        self.linked.append(self.item_1)
        self.linked.append(self.item_2)
        self.linked.append(self.item_3)
        self.linked.remove(self.item_2)
        self.assertEqual(self.linked.size, 2)
        self.assertEqual(self.linked.first_item, self.item_1)
        self.assertEqual(self.linked.last_item, self.item_3)

def main_test():
    unittest.main()

if __name__ == "__main__":
    ops = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    ops = ["LRUCache","put","put","get","put","put","get"]
    values = [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]


    print(main(ops, values))
    #main_test()