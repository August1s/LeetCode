


def removeElement(nums: list, val: int) -> int:
    '''
    for index in range(len(nums)-1,-1,-1):
        if nums[index] == val:
            nums.pop(index)
    return len(nums)'''
    # 双指针解法
    if nums == []: return 0
    i=0
    for j in range(0,len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i+=1
    return i


nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums,val))
print(nums)