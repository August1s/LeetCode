


def twoSum(nums: list, target: int) -> list:
    
    dic = {} # 构造一个字典，如果要找y，用target-x作为key在字典中去找y
    '''
    for i in range(len(nums)):
        dic[nums[i]] = i
    for num in nums:
        if target-num in dic.keys() and dic[target-num] != nums.index(num):
            return [nums.index(num),dic[target-num]]   '''

    # 由于只在一个list里找，且求的是 “两数”之和，可以先在dic里面记一个
    # 比如，当num=2时，target-num (6-2=4) 不在dic中，就可以先把i和num=2存进去
    # 遍历到num=4时，target-num (6-4=2) 已在dic中
    # 这样边遍历边构建可以减少内存
    for i,num in enumerate(nums):
        if  target-num in dic.keys():
            return [dic[target-num],i]
        dic[num]=i
    return []
    



nums = [1,2,3,3,7]
target = 6

print(twoSum(nums,target))