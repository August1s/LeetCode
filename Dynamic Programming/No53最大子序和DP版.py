

# 使用动态规划求解最大子序和问题
def maxSubArray(nums):

    # 状态转移方程的递归解法
    # 不过这里不能用递归解法，因为求的是最大值，而不一定是最后的值
    # 除非用一个全局变量记录一下
    #res = Rec_maxSubArray(nums, len(nums)-1)

    res = DP_maxSubArray(nums)

    return res


def Rec_maxSubArray(nums, i):
    if i == 0 :
        return nums[i]
    else:
        A = Rec_maxSubArray(nums, i-1) + nums[i]
        B = nums[i]
        # print(max(A ,B))  ->状态转移方程
        return max(A, B)


def DP_maxSubArray(nums):
    '''
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1, len(nums)-1):
        A = dp[i-1]+ nums[i]
        B = nums[i]
        dp[i] = max(A, B)
    return max(dp)
    '''
    # 由于状态转移方程只牵扯到两个量，因此可以用变量来记录前一个状态和最终结果
    dp = nums[0]
    res = dp
    for i in range(1, len(nums)):
        A = dp+ nums[i]
        B = nums[i]
        dp = max(A, B)
        print(dp)
        res = max(res, dp)
    return res


nums = [-2,1]
print(maxSubArray(nums))