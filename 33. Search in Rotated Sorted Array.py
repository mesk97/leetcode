def search(nums, begin_index, end_index, target):
    while ((end_index - begin_index) >= 2):
        middle = int((end_index + begin_index)/2)

        if nums[begin_index] < nums[end_index]:
            if nums[middle] >= target:
                end_index = middle
            else:
                begin_index = middle
            continue
    
    if nums[begin_index] == target:
        return begin_index
    if nums[end_index] == target:
        return end_index
    return -1

def find_top(nums):
    begin_index = 0
    end_index = len(nums) - 1

    while ((end_index - begin_index) >= 2):
        middle = int((end_index + begin_index)/2)
        if nums[middle] < nums[begin_index]:
            end_index = middle
        else:
            begin_index = middle
    
    if nums[begin_index] > nums[end_index]:
        return begin_index
    return end_index

def main(nums, target):
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        if nums[0] == target:
            return target
        return -1

    top = find_top(nums)
    if target <= nums[top] and target >= nums[0]:
        return search(nums, 0, top, target)

    if top == (len(nums) - 1):
        return -1
    return search(nums, top+1, len(nums)-1, target)

if __name__ == "__main__":
    nums = [4,5,6,7,8,1,2,3]

    target = 5
    print (main(nums, target))