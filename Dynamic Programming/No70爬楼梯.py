

def climbStairs(n: int) -> int:
    
    #res = Rec_climbStairs(n)
    res = DP_climbStairs(3)
    return res


# 递归解法,会超时
def Rec_climbStairs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return Rec_climbStairs(n-1) + Rec_climbStairs(n-2) # ->状态转移方程

# DP解法
def DP_climbStairs(n):
    dp1, dp2, dp = 1, 2, 0
    if n == 1 : return dp1
    elif n == 2: return dp2
    for _ in range(3, n+1):
        dp = dp1 + dp2
        dp1 = dp2
        dp2 = dp
    return dp


print(climbStairs(3))