

# 如果直接按照最大子序和的思路，会发现无法找到最优子结构，因为有可能是负数，但是负负得正
# 因此，需要记录两个状态转移，一个记录正数，一个记录负数
# 判断正数的状态转移的时候考虑nums[i]为负数的情况


def maxProduct(self, nums: List[int]) -> int:
    n = len(nums)
    dpPos = [0]*n
    dpNeg = [0]*n

    dpPos[0] = dpNeg[0] = nums[0]
    for i in range(1, n):
        dpPos[i] = max(dpPos[i-1]*nums[i], nums[i], dpNeg[i-1]*nums[i]) #<----
        dpNeg[i] = min(dpPos[i-1]*nums[i], nums[i], dpNeg[i-1]*nums[i])

    return max(dpPos)