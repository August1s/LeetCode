

# 状态转移方程 F[i] = F[i-1] + F[i-2]，表示第i位使用一位数解码或使用两位数解码
# 但是两个状态需要一些条件才能被计算
# i处使用一位数，必须保证非0才能解码
# i处使用两位数，必须保证该两位数小于等于26

def numDecodings(self, s: str) -> int:
    n = len(s)
    dp = [0]*n
    if s[0] == '0' or s == "":
        return 0
    elif n == 1:
        return 1
    
    dp[0] = 1
    if s[1] != '0':
        dp[1] += 1
    if int(s[0:2]) <= 26:
        dp[1] += 1

    for i in range(2, n):
        if s[i] != '0':
            dp[i] += dp[i-1]
        if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
            dp[i] += dp[i-2]
        
    return dp[-1]