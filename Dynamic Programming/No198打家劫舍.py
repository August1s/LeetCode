
'''
# 状态转移方程 F[i] = nums[i] + max(F[i-2], F[i-3])  -->有点问题

# 实际上的正确的转移方程 F[i] = max(F[i-1], G[i-1])
#                      G[i] = max(F[i-1], nums[i-1])

# F表示不选第i个数的状态，G表示选择第i个数的状态



def rob(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [0]*n
    if n==0: return 0
    if n==1: return nums[0]
    if n==2: return max(nums)
    dp[0], dp[1], dp[2] = nums[0], max(nums[0], nums[1]), max(nums[1], nums[0]+nums[2])

    for i in range(3, n):
        dp[i] = nums[i] + max(dp[i-2], dp[i-3])

    return max(dp[-1], dp[-2])
'''

# 一个转移方程更清晰的版本
# F[i] = max(F[i-1], nums[i]+F[i-2])
# 可以看出这个转移方程的意义是，选择nums[i]或者不选nums[i]

def rob(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [0]*n
    if n==0: return 0
    if n==1: return nums[0]
    if n==2: return max(nums)
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], nums[i]+dp[i-2])

    return dp[-1]