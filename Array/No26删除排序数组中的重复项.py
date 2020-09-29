


def removeDuplicates(nums) -> int:
    '''
    # 由于删除操作会导致数组变化，所以反向遍历，这样前边元素下标不变
    for index in range(len(nums)-1,0,-1):
        
        if nums[index] == nums[index-1]:
            nums.pop(index)
    return len(nums)'''
    # 题目说明不用考虑新长度之后的元素，所以可以使用双指针记录位置
    if nums == []: return 0
    i = 0
    for j in range(1,len(nums)):
        if nums[j]!=nums[i]:
            i += 1
            nums[i] = nums[j]

    return i+1


nums = [1,1,2]
print(removeDuplicates(nums))
print(nums)