# two pointers

# https://leetcode.com/problems/trapping-rain-water/description/
# 42. Trapping Rain Water
# Hard
# Topics
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

def add_volume(height, old_begin_hight, old_end_hight, begin, end):
    volume = (end - begin - 1) * (min(height[begin], height[end]) - min(old_begin_hight, old_end_hight) )
    return volume

def calc_volume(height, begin, end, high_begin, high_end):
    # рассмотрим следующие случаи 
    # 0. первичное заполнение -> заполнить по наименьшей стенке
    if begin == high_begin and end == high_end:
        return add_volume(height, 0, 0, high_begin, high_end)

    # 1. выросла одна из стенок -> дополнить по дельте роста
    # и еще и вычесть эту стенку в прошлом наливе 
    if height[begin] > height[high_begin]:
        return add_volume(height, height[high_begin], height[high_end], begin, high_end) - height[high_begin]
    if height[end] > height[high_end]:
        return add_volume(height, height[high_begin], height[high_end], high_begin, end) - height[high_end]

    # 2. движение без роста стенок -> вычесть на величину стенки
    if begin > high_begin:
        return -height[begin]
    if end < high_end:
        return -height[end]
    
    # невозможно 
    print ("АЛЕРТ !!")
    return 0

def main(height):
    begin = 0
    end = len(height) - 1
    result = 0

    high_begin = begin
    high_end = end
    
    while end > begin:
        # Добавляем воды или уменьшаем ее 
        add_volume = calc_volume(height, begin, end, high_begin, high_end)
        result = result + add_volume
        
        # переносим высокую стенку 
        if height[begin] > height[high_begin]:
            high_begin = begin
        if height[end] > height[high_end]:
            high_end = end

        # двигаем меньшую стенку
        if height[high_begin] < height[high_end]:
            begin = begin + 1
        else:
            end = end - 1

    return result


if __name__ == "__main__":
    height = [4,2,0,3,2,5]
    #height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(main(height))