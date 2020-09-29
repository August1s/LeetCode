

'''
# 循环解法
def countAndSay(n) -> str:
    if n==1:
        return '1'
    s1 = '11'
    s2 = ''
    for i in range(2,n):
        p = 1
        for q in range(0,len(s1)-1):
            if s1[q] == s1[q+1]:
                p += 1
            else:
                s2 = s2 + str(p) + s1[q]
                p = 1
        s2 = s2 + str(p) + s1[-1]
        s1 = s2
        s2 = ''

    return s1
'''


# 递归解法
def countAndSay(n) -> str:
    if n <= 1 :
        return '1'

    s1 = countAndSay(n-1)·  
    s2 = ''
    count = 1
    for q in range(0,len(s1)-1):
        if s1[q] == s1[q+1]:
            count += 1
        else:
            s2 = s2 + str(count) + s1[q]
            count = 1
    s2 = s2 + str(count) + s1[-1]

    return s2



for i in range(1,31):
    print(countAndSay(i))



