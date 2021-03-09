
# 一个直接想到的放法是用2循环求余
def hammingWeight(self, n: int) -> int:
    count = 0
    while n!=0:
        c = n%2
        if c==1:
            count+=1
        n = n//2

    return count


# 实际上直接使用位运算判断是最快的
def hammingWeight(self, n: int) -> int:
    count = 0
    while n!=0:
        count += n & 1
        n = n >> 1
    return count