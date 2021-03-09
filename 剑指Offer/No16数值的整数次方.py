

# 直接循环会超时。复杂度O(n)
# 注意到，pow(3,6) = pow(9,3) = 9*pow(81*1)
# 也就是 pow(x, n) = pow(x*x, n//2) 或 x * pow(x*x, n//2)
# 时间复杂度是O(logn)      


def myPow(self, x: float, n: int) -> float:
    
    def Rec(i, j):
        if j==0:
            return 1
        if j==1:
            return i
        if j==-1:
            return 1/i
        if j%2==0:
            return Rec(i*i, j//2)
        else:
            return i*Rec(i*i, j//2)

    return Rec(x,n)