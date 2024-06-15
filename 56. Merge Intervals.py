# https://leetcode.com/problems/merge-intervals/description/

# 56. Merge Intervals
# Medium
# Topics
# Companies
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2.4M
# Submissions
# 5.1M
# Acceptance Rate
# 47.5%
# Topics
# Array
# Sorting

# первая попытка 
# Input
# intervals =
# [[1,4],[2,3]]

# Use Testcase
# Output
# [[1,3]]
# Expected
# [[1,4]]

# не очень результат
# по сути можно пробовать 
# 1. без сортировки ?
# делать плоский массив ? 


# Runtime
# 128
# ms
# Beats
# 30.87%
# Analyze Complexity
# Memory
# 21.17
# MB
# Beats
# 20.90%


# по скорости полная чушь !! 
# Runtime
# 118
# ms
# Beats
# 80.94%


def main(intervals):
    results = []

    # получаем сортированный список по стартовой точке 
    intervals.sort(key=lambda i: i[0])
    results = [intervals[0]]

    for start, end in intervals:
        last = results[-1]
        if last[1] < start:
            # добавляем 
            results.append([start, end])
            continue

        # мержим -> по сути обновляем конечную точку
        if end > last[1]:
            last[1] = end

    return results

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(main(intervals))