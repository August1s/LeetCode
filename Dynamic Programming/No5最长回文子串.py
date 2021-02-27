

# 朴素的动态规划法，超时。。
# 状态转移方程： F[i][j] = F[i+1][j-1] && S[i]==S[j]
# [i,j]区间内的字符串是否是一个回文串，取决于[i+1,j-1]是否是一个回文串。以及第i个字符和第j个字符是否相等
# 如果是单个字符，则一定是回文字符串
# 如果是两个字符，则两个字符相等为回文字符串

# 面对区间选择问题，一般都是，先穷举区间长度，再枚举左端点，然后分别判断子问题情况


def longestPalindrome(self, s: str) -> str:
    n = len(s)
    dp = [[False]*n for _ in range(0, n)]
    res = ""

    for length in range(n):
        for i in range(n):
            j = i + length
            if j>=n:
                break
            if i==j:
                dp[i][j] = True
            elif j==i+1:
                dp[i][j] = s[i]==s[j]
            else:
                dp[i][j] = dp[i+1][j-1] and s[i]==s[j]

            if len(res)<length+1 and dp[i][j]:
                res = s[i:j+1]

    return res