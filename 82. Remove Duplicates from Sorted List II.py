# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/?envType=study-plan&id=algorithm-ii
# 82. Remove Duplicates from Sorted List II
# Medium
# 7K
# 186
# Companies
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# def fromListNode(head):
#     result = []
#     while head is not None:
#         result.append(head.val)
#         head = head.next 
#     return result

# def toListNode(result):
#     last_node = None
#     for i in reversed(result):
#         last_node = ListNode(i, last_node)
#     return last_node

def main(nums):
    result = []
    checked = None 
    checked_double = False
    current = 0

    while current < len(nums):
        if checked is not None:
            if nums[current] == checked:
                checked_double = True
            else:
                if not checked_double:
                    result.append(checked)
                checked_double = False
                checked = nums[current]            
            
        checked = nums[current]
        current = current + 1
    
    if checked is not None and not checked_double:
        result.append(checked)

    return result


if __name__ == "__main__":
    head = [1,1,3,4,4,5,6, 6]
    print(main(head))