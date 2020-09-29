


# 这显然是一个二分查找


def searchInsert(nums, target: int) -> int:
    n = len(nums)
    l=0
    r=n-1

    while(l<=r):
        mid = (l+r)//2
        if nums[mid]==target:
            # 由于题目给定了无重的条件，可以直接返回
            return mid
        elif nums[mid] > target:
            r = mid-1
        else:
            l = mid+1

    return l

print(searchInsert([1,3,5,6],0))