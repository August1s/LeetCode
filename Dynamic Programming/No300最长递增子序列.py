
# 令F[i]为以i为结尾的子序列的最大长度
# 令k为子序列的倒数第2个元素，显然，这里k一共有i-1种取值，因此需要枚举
# 状态转移： F[i] = max(F[k] + 1) （当nums[i]>numsk[k]时）


def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1]*n 
    for i in range(1, n):
        for j in range(0, i):
            if nums[j]<nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)