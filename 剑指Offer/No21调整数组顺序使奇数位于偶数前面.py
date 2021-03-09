

# 使用快慢指针，快指针指向奇数，慢指针指向偶数

def exchange(self, nums: List[int]) -> List[int]:
    p = 0
    while p<len(nums):
        if nums[p]%2==0:
            break
        else:
            p += 1
    q = p
    while q<len(nums):
        if nums[q]%2 == 1:
            break
        else:
            q += 1


    while p<len(nums) and q<len(nums):
        nums[p], nums[q] = nums[q], nums[p]
        p += 1
        while q<len(nums):
            if nums[q]%2 == 1:
                break
            else:
                q += 1

    return nums