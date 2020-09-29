

'''
# 循环逐位运算
def addBinary(a: str, b: str) -> str:
    if len(a)<len(b):
        a = '0' * (len(b)-len(a)) + a
    else:
        b = '0' * (len(a)-len(b)) + b

    i, res, c = len(a)-1, "", 0
    while i>=0 :
        if i == len(a)-1:
            res, c = str((int(a[i]) + int(b[i])) % 2) + res, (int(a[i]) + int(b[i])) // 2
        else:
            res, c = str((int(a[i]) + int(b[i]) + c) % 2) + res, (int(a[i]) + int(b[i]) + c) // 2
        i -= 1
    if c != 0:
        res = str(c) + res
    return res'''

# 位操作解法
# x xor y 可以得到两数的无进位相加结果
# (x and y) << 1 与操作左移可以得到进位结果
def addBinary(a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        print(x,y)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]


print(addBinary("1111","1011"))
