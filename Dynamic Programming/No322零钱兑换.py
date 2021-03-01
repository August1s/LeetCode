

# 状态转移方程 F[i] = min(F[i - Ck] + 1)
# F[i]表示i块钱需要的硬币数量，Ck表示第k个硬币


def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [10001]*(amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for c in coins:
            if i>=c:
                dp[i] = min(dp[i], dp[i-c]+1)
    return dp[amount] if dp[amount]!=10001 else -1