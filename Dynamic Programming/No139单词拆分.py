

# 以字符串分界点的不同作为状态的不同划分(在一个循环中实现)
# 以一个字符串划分后的结果（bool)进行状态转移

# F[i] = F[k-1] && check(s[k...i])


def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    n = len(s)
    dp = [False]*n
    dp[0] = (s[0] in wordDict)
    for i in range(1, n):
        for k in range(0, i+1):
            if k == 0:
                dp[i] = s[k:i+1] in wordDict
            else:
                dp[i] = dp[i] or ( dp[k-1] and (s[k:i+1] in wordDict))

    return dp[-1]