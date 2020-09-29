'''
# 暴力解法
def maxSubArray(nums):
    tmp = nums[0]
    maxsum = tmp
    for i in range(1, len(nums)):
        if tmp+nums[i] > nums[i]:
            tmp = tmp+nums[i]
            maxsum = max(maxsum, tmp)
        else:
            maxsum = max(maxsum, tmp, nums[i])
            tmp = nums[i]

    return maxsum'''


# 分治法求解
def maxSubArray(nums):
    _, _, res = FindMaxSum(nums,0,len(nums)-1)
    return res
def FindMaxSum(nums, low, high):
    if high == low:
        return low, high, nums[low]
    else:
        mid = (high+low) // 2
        leftlow, lefthigh, leftsum = FindMaxSum(nums, low, mid)
        rightlow, righthigh, rightsum = FindMaxSum(nums, mid+1, high)
        crosslow, crosshigh, crosssum = FindMaxCrossSum(nums, low, mid, high)
        if leftsum >= rightsum and leftsum >= crosssum:
            return leftlow, lefthigh, leftsum
        elif rightsum >= leftsum and rightsum >= crosssum:
            return rightlow, righthigh, rightsum
        else:
            return crosslow, crosshigh, crosssum
#寻找跨越了中点的最大子数组
def FindMaxCrossSum(nums, low, mid, high):
    leftsum, rightsum = -99999, -99999
    maxlift,maxright = low, high
    sum = 0
    for i in range(mid, low-1, -1):
        sum += nums[i]
        if sum > leftsum:
            leftsum, maxlift = sum, i
    sum = 0
    for i in range(mid+1, high+1):
        sum += nums[i]
        if sum > rightsum:
            rightsum, maxright = sum, i
    return maxlift, maxright, leftsum+rightsum



l = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(l))