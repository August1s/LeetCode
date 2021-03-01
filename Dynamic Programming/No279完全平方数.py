

# 动态规划
# 状态转移方程： F[i] = min( F[i-k^2]+1)
# F[i] 代表i需要的平方数的个数，而i可能由若干种平方数k^2构成
# 这意味着我们需要枚举 k^2
def numSquares(self, n: int) -> int:
    dp = [10000]*(n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        for k in range(1, i):
            if k*k > i:
                break
            dp[i] = min(dp[i], dp[i-k*k] + 1)

    return dp[n]







