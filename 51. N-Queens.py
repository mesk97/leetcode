# https://leetcode.com/problems/n-queens/description/
# 22.10
# 22.22 - готов алго 
# 23.21 - реализован
# try 1 - без единого бага прошел тесты - только результаты фиговые
# Runtime  73 ms Beats 33.91% of users with Python3
# Memory 19.08 MB Beats 7.14% of users with Python3
# try 2 - оптимизация ... 
# Runtime 63 ms Beats 42.78% of users with Python3

# algo
# main:
#     item=get_from_stack
#     if is_final
#         report
#     check_same_position
#     if not find_next_to_place:
#         continue
#     update_item
#     put_to_stack

# find_next_to_place
#     find_in_next_row
#     find_in_next_column
#     check_bitie
#         in set row
#         in set col
#         in set diag_left
#             diag_left = row - col
#         in set diag_right
#             diag_right = row + col

# 51. N-Queens
# Hard
# Topics
# Companies
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]
 

# Constraints:

# 1 <= n <= 9
# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Accepted
# 687K
# Submissions
# 1M
# Acceptance Rate
# 67.7%
# Topics
# Array
# Backtracking

class Item:
    def __init__(self, nsize, row):
        self.nsize = nsize
        self.row = row

        self.queens = list()

        #self.busyRows = set()
        self.busyCols = set()
        self.busyDiagsLeft = set()
        self.busyDiagsRight = set()
        pass

    # def getSign(self):
    #     return str(self.queens)
    
    def isFinal(self):
        return self.row == (self.nsize - 1)

    def _getFree(self, col, row):
        # проверяем что позиция бьется другими ферзями в этой ветке
        # если в том же ряду или колонке - то тут понятно
        # диагонали вычисляем так:
        #  1.1 диагонали паралельные C1R4-C4R1 назову right правыми, верхушка справа
        #  1.2 чтобы понять что клетки принадлежат одной диагонали (например X, Y)
        #  1.3 нужно сравнить суммы X = С3+R1 и Y = С1+R3 и если равны то одна диагональ
        #  2.1 диагонали паралельные C1R1-C4R4 назову left левыми, верхушка слева
        #  2.2 чтобы понять что клетки принадлежат одной диагонали (например Z, W)
        #  2.3 нужно сравнить разницы Z=R1-C2 и W=R3-C4   
        #     C1 C2 C3 C4
        #   R1 _  Z  X  _
        #   R2 _  _  _  _
        #   R3 Y  _  _  W
        #   R4 _  _  _  _

        #if row in self.busyRows:
        #    return None
        #if col in self.busyCols:
        #    return None
        diagRight = col + row
        if diagRight in self.busyDiagsRight:
            return None
        diagLeft = row - col
        if diagLeft in self.busyDiagsLeft:
            return None

        # ускоритель
        new_queens = self.queens.copy()
        new_queens.append(col)
        sign = str(new_queens)

        global cache
        if sign in cache:
            return None
        cache.add(sign)

        # копируем 
        new_item = Item(self.nsize, row)
        #new_item.queens = self.queens.copy()
        new_item.queens = new_queens
        #new_item.busyRows = self.busyRows.copy()
        new_item.busyCols = self.busyCols.copy()
        new_item.busyDiagsLeft = self.busyDiagsLeft.copy()
        new_item.busyDiagsRight = self.busyDiagsRight.copy()

        # апдейтим используемое 
        #new_item.queens.append(col)
        #new_item.busyRows.add(row)
        new_item.busyCols.add(col)
        new_item.busyDiagsLeft.add(diagLeft)
        new_item.busyDiagsRight.add(diagRight)

        return new_item

    def findNext(self):
        next_items = []
        next_row = self.row + 1

        global nsize_set
        diff_set = nsize_set - self.busyCols

        #for col in range(0, self.nsize):
        for col in diff_set:
            next = self._getFree(col, next_row)
            if not next is None:
                next_items.append(next)
        return next_items

    def report(self):
        # у нас все по рядам
        result = []
        for qcol in self.queens:
            str = ''.join(['.' * qcol]) + 'Q' + ''.join(['.' * (self.nsize - qcol - 1)])
            result.append(str)
        return result

def main(n):
    stack = []
    result = []

    global cache
    cache = set()

    global nsize_set
    nsize_set = set()
    for i in range(0, n):
        nsize_set.add(i)

    stack.append(Item(n, -1))
    while len(stack) > 0:
        item = stack.pop()
        
        # ускоритель
        #if item.getSign() in cache:
        #    continue
        #cache.add(item.getSign())
        
        if item.isFinal():
            result.append(item)
            continue

        new_items = item.findNext()     
        stack.extend(new_items)

    reported_result = []
    for item in result:
        reported_result.append(item.report())
    return reported_result

if __name__ == "__main__":
    n = 5
    # Output: [
    #     [".Q..",
    #      "...Q",
    #      "Q...",
    #      "..Q."],
    #     ["..Q.",
    #      "Q...",
    #      "...Q",
    #      ".Q.."]]
    print(main(n))