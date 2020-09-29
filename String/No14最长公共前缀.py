


# zip()函数：用于将可迭代的对象作为参数
# zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。
# 若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。利用*号操作符，可以将list unzip（解压）。

def longestCommonPrefix(strs) -> str:
    result = ""
    for i in zip(*strs):
        if len(set(i)) == 1:
            result += i[0]
        else:
            break
    return result


l1 = [1,2,3]
l2 = ['abc',(1,2,3),[3,4,5,6]]
l3 = [9,8,7,6]
for i in zip(*l2):
    print(i)

haystack = "hello"
needle = "ll"

print(haystack.find(needle))