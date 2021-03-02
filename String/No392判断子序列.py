


# 一个朴素的想法是使用双指针
def isSubsequence(self, s: str, t: str) -> bool:
    p, q = 0, 0
    while(p<len(s) and q<len(t)):
        if s[p] == t[q]:
            p += 1
            q += 1
        else:
            q += 1
    return p==len(s)


# 题目的进阶要求：
# 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，怎样改变代码？

# 在双指针做法中可以看出，q是需要一直循环的
# 因此可以预先对字符串T进行处理，使用一张二维表记录一下从第i个字符到第j个字符的距离差，这显然是一个动态规划的过程
# 这样我们就可以在满足进阶要求，在线性时间内判断S