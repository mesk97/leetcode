# https://leetcode.com/problems/subsets-ii/description/
# 15.35
# 15.40 - понятен алгоритм
# 15.52 - локальный дебуг
# 16.02 - 15 / 20 testcases passed  -> были дупликаты изза отсутствия сортировки
#       2 раза здесь болтался
    # Input
    # nums =
    # [4,4,4,1,4]
    # Use Testcase
    # Output
    # [[],[4],[1],[1,4],[4,4],[4,1],[4,1,4],[4,4,4],[4,4,1],[4,4,1,4],[4,4,4,1],[4,4,4,4],[4,4,4,1,4]]
    # Expected
    # [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
# 16.15  - ok но плохие значения 
# Runtime 43 ms 
# Beats 33.44% of users with Python3
# Memory 17.00 MB
# Beats 21.25% of users with Python3

# делаем стэк
# дак каждым элементом
# перебираем последовательно элементы массива впереди 
# проверяем 
#    репортился ли
# репортим + складываем в стэк на дальше 

# 90. Subsets II
# Medium
# Topics
# Companies
# Given an integer array nums that may contain duplicates, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Accepted
# 875.1K
# Submissions
# 1.5M
# Acceptance Rate
# 57.1%
# Topics
# Array
# Backtracking
# Bit Manipulation

def main(nums):
    result = list()
    result.append(list())

    stack = list()
    stack.append((list(), 0))

    passed = set()

    while len(stack) > 0:
        #(old_item, pointer) = stack.pop()

        # важно пропускать самые первые серии вперед иначе заглушат более девнии развитие 
        (old_item, pointer) = stack[0]
        del stack[0]

        for i in range(pointer, len(nums)):
            # добавляем новый элемент и магия с tuple -> потому что list - unhashable элемент
            item = list(old_item)
            item.append(nums[i])
            item = tuple(sorted(item))

            # ускоряем и убираем дупликаты
            if item in passed:
                continue
            passed.add(item)

            # новый сабсет
            result.append(list(item))

            # продолжаем
            stack.append((item, i + 1))

    return result

if __name__ == "__main__":
    nums = [1,2,2]

    nums = [4,4,4,1,4]
    # Output   [[],[4],[1],[1,4],[4,4],[4,1],[4,1,4],[4,4,4],[4,4,1],[4,4,1,4],[4,4,4,1],[4,4,4,4],[4,4,4,1,4]]
    # Expected [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]

    print(main(nums))