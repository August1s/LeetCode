
# 如果使用遍历的线性方法寻找的话，时间复杂度是O(n)

# 由于是递增序列，因此可以通过二分查找判断旋转点（也就是要求的最小数字），复杂度是O(logn)

# 旋转将数组分为两段，递增序列保证前一段的值一定大于等于后一段
# 假设端点i,j，中点mid
# 如果num[j]<num[mid]，说明此时的mid一定在旋转点之前，因此i=mid+1
# 如果num[j]<num[mid]，说明此时的mid一定在旋转点之后，因此j=mid  -->（这里不+1是因为有可能越过旋转点）
# 如果num[j]==num[mid]，无法判断mid在旋转点前后，因此缩小j

def minArray(self, numbers: List[int]) -> int:
    i, j = 0, len(numbers)-1
    while i<j:
        mid = (i+j)//2
        # print(i, j, mid)
        if numbers[j] < numbers[mid]:
            i = mid+1
        elif numbers[j] > numbers[mid]:
            j = mid
        else:
            j -= 1

    return numbers[i]