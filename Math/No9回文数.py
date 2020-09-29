


# 不用字符串
'''
def isPalindrome(x: int) -> bool:
    if x<0 :
        return False
    a = x
    result = 0
    c = 0 # 位数
    while(a!=0):
        c = a%10
        a = a//10
        result = result*10+c
    return True if result == x else False'''

# 回文数可以只判断一半位数
def isPalindrome(x: int) -> bool:
    if x<0 or (x%10 == 0 and x!=0):
        return False
    result = 0
    while(x>result): # 将x的位给result，当result>x表示已经过了一半
        result = result*10 + x%10
        x = x//10
    # x可能长度为奇数，也可能为偶数
    # 长度偶数时，直接判断result和x，奇数时，需要除掉result的最后一位
    return x == result or x == result//10 

print(isPalindrome(1001))