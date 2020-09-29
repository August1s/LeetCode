

# 使用二分法
'''
def mySqrt(x: int) -> int
    if x == 1 or x == 0:
        return x
    start, end, mid = 0, x, x//2
    while(mid != end and mid != start):
        if mid * mid > x:
            start, end = start, mid
            mid = (end+start)//2
        elif mid * mid < x:
            start, end = mid, end
            mid = (end+start)//2
        else:
            return mid

    return mid'''

# 递归解法
def mySqrt(x: int) -> int:
    if x == 1 or x == 0:
        return x
    return Devide(0, x, x//2, x)

def Devide(start, end, mid, target):
    if mid == end or mid == start or mid * mid == target:
        return mid
    if mid * mid > target:
        return Devide(start, mid, (mid+start)//2, target)
    else:
        return Devide(mid, end, (mid+end)//2, target)


print(mySqrt(250))