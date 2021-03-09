


# 状态转移方程：F(i,j) = p[j]不是*的时候  F(i-1, j-1) && (s[i]==p[j])
#                     = p[j]是*的时候  F(i-1, j) && (s[i]==p[j-1]) 或 F(i,j-2) 

# 当p[j]不是*的时候，直接匹配即可，结果取决于F(i-1, j-1)
# 当p[j]是*的时候有两种情况：
# 1.p[j-1]*代表空字符串的时候，此时结果就是 F(i,j-2) 
# 2.p[j-1]*代表一个以上p[j-1]的时候，匹配s[i]和p[j-1]，同时这个结果取决于F(i-1, j)
def isMatch(self, s: str, p: str) -> bool:
    m = len(s)
    n = len(p)
    dp = [[False]*(n+1) for _ in range(m+1)]
    s = ' '+s
    p = ' '+p        

    for i in range(0, m+1):
        for j in range(0, n+1):
            if i==0 and j==0:
                dp[i][j] = True
            else:
                if p[j] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i]==p[j] or (p[j]=='.' and s[i]!=' '))
                else:
                    if j>=2:
                        dp[i][j] = dp[i][j] or dp[i][j-2]
                    if i>=1 and j>=1 and (s[i]==p[j-1] or p[j-1]=='.'):
                        dp[i][j] = dp[i][j] or dp[i-1][j]

    return dp[-1][-1]