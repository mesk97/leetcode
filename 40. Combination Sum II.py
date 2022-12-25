# https://leetcode.com/problems/combination-sum-ii/?envType=study-plan&id=algorithm-ii

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

class Item:
    def __init__(self, value, place, prev):
        self.value = value
        self.place = place
        self.prev = prev


def how_many_to_add(item: Item, value, target):
    result = [value]
    sum = target - value
    while item != None:
        if (item.value != 0):
            result.append(item.value)
        sum = sum - item.value
        item = item.prev
    return (sum, result)

    # sorted list 
    # work with elements 
    # keep in stack valid chains
    #  candidate -> candidate -> candidate
    #  chain
    #    value, place, prev
    # for each chain
    #     place + 1, len - except with similar value 
    #     check chain + element -> == !!, < -> puth to stack, > - skip
def main(_candidates, target):
    result = []
    candidates = sorted(_candidates)
    stack = [Item(0, -1, None)]

    while len(stack) > 0:
        item = stack[0]
        last_value = None
        for i in range(item.place + 1, len(candidates)):
            value = candidates[i]
            if value == last_value:
                continue
            last_value = value
            (checked, r) = how_many_to_add(item, value, target)
            if checked == 0:
                result.append(r)
            elif checked > 0:
                stack.append(Item(value, i, item))
        del stack[0]

    return result


if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(main(candidates, target))