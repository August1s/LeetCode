
# 和正常的打家劫舍I相比，nums变成了环，这意味着首尾元素不能同时选择
# 因此分为两种情况
# 一种是选择nums[0],一种是不选择nums[0]
# 这样就可以转化为两个 打家劫舍I

def rob(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [0]*n
    if n==0: return 0
    if n==1: return nums[0]
    if n==2: return max(nums)

    # 抢第一家
    dp[0], dp[1]= nums[0], nums[0]
    for i in range(2, n-1):
        dp[i] = max(dp[i-1], nums[i]+dp[i-2])
    A = dp[n-2]

    # 不抢第一家
    dp[0], dp[1] = 0, nums[1]
    for i in range(2, n):
        dp[i] = max(dp[i-1], nums[i]+dp[i-2])
    B = dp[-1]

    return max(A,B)