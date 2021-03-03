
# 如果对空间有要求，可能需要使用双指针法或者先排序后查找相邻元素的方法

def findRepeatNumber(self, nums: List[int]) -> int:
    h = {}
    for i in nums:
        if i in h.keys():
            return i
        else:
            h[i] = 1
    return -1