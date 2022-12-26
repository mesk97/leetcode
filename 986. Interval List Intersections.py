# https://leetcode.com/problems/interval-list-intersections/?envType=study-plan&id=algorithm-ii
# 986. Interval List Intersections
# Medium
# 4.9K
# 95
# Companies
# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

# Example 1:
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

# search until there is first or second
# detect intersect 
# if 0  sravnivaem  first 
# if >0 srafnivaem konci 

def getFromList(list):
    if len(list) == 0:
        return None
    item = list[0]
    del list[0]
    return item

def doInterSect(first, second):
    if first[1] < second[0] or second[1] < first[0]:
        return None
    return [max(first[0], second[0]), min(first[1], second[1])]

def main(firstList, secondList):
    result = []

    first = getFromList(firstList)
    second = getFromList(secondList)

    #print(first, second)

    while first is not None and second is not None:
        intersect = doInterSect(first, second)

        print(first, second, intersect)

        if intersect == None:
            if first[1] > second[1]:
                second = getFromList(secondList)
            else:
                first = getFromList(firstList)
        else:
            result.append(intersect)
            if second[1] > first[1]:
                first = getFromList(firstList)
            else:
                second = getFromList(secondList)

    return result

if __name__ == "__main__":
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    print (main(firstList, secondList))