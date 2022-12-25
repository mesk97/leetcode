def is_pike(begin_index, middle, end_index, nums):
    if nums[middle] > nums[begin_index] and nums[middle] > nums[end_index]:
        return True
    return None
    
def main(nums):
    begin_index = 0
    end_index = len(nums)-1

    while begin_index < end_index-2:
        middle = int((end_index + begin_index)/2)

        if nums[end_index] > nums[middle] or nums[middle+1] > nums[middle]:
            begin_index = middle
            continue

        if nums[begin_index] > nums[middle] or nums[middle-1] > nums[middle]:
            end_index = middle
            continue

        if is_pike(begin_index, middle, end_index, nums):
            return middle

        # here  begin == middle == end 
        # need to do recursive 
        pike1 = main(nums[begin_index:middle-1])
        pike2 = main(nums[middle+1:end_index])
        if nums[pike1] > nums[pike2]:
            return pike1
        return pike2

    middle = int((end_index + begin_index)/2)
    if is_pike(begin_index, middle, end_index, nums):
        return middle
    
    if nums[begin_index] > nums[end_index]:
        return begin_index
    return end_index

if __name__ == "__main__":
    nums = [1]
    print(main(nums))