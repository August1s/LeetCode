# 一个比较容易想到的方法是使用一个hash记录次数
def singleNumber(self, nums: List[int]) -> int:
    h={}
    for i in nums:
        if not i in h.keys():
            h[i] = 1
        else:
            h[i] += 1

    for i in h.keys():
        if h[i] == 1:
            return i


# 如果要在O(1)格外空间内进行判断，只能使用异或进行运算。
# （因为题目规定了元素最多出现两次，且只有一个元素出现一次）
# 任何数和其自身做异或运算，结果是0；任何数和0做异或运算，结果仍然是原来的数。
# 因此，只要在这个数组中，全部元素做异或，最后的结果就是出现一次的数字。
def singleNumber(self, nums: List[int]) -> int:
    def fun(x,y):
        return x^y
    return reduce(fun, nums)