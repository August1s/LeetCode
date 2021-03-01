

# 状态转移方程：F[i] = max{k(i-k), k*F[i-k]}
# i一共可以拆为k和i-k，要么直接计算k(i-k)，要么继续拆，也就是F[i-k]，然后取值大的那个


def integerBreak(self, n: int) -> int:
    dp = [0]*(n+1)
    dp[0],dp[1] = 0, 1
    for i in range(2, n+1):
        for k in range(1, i):
            dp[i] = max(dp[i], k*(i-k), k*dp[i-k])

    return dp[n]


# 其实实际上只有4，5，6三个数是有选择了k(i-k)的情况，因此也可以直接判断
def integerBreak(self, n: int) -> int:
    dp = [0]*(n+1)
    dp[0],dp[1] = 0, 1
    for i in range(2, n+1):
        if i==4:
            dp[i] = 4
        elif i==5:
            dp[i] = 6
        elif i==6:
            dp[i] = 9

        for k in range(1, i):
            dp[i] = max(dp[i], k*dp[i-k])

    return dp[n]