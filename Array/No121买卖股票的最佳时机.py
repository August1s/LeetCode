
# 记录买入日期（股价最小）和利润
# 如果第二天的股价更大，则比较利润
# 如果第二天的股价更小，则比较买入日期
# 实际上是相当于动态规划中使用两个状态以及状态转移

def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)

    min_index = 0
    res = 0
    for i in range(1, n):
        
        if prices[i]>=prices[i-1]:
            res = max(res, prices[i] - prices[min_index])
        else:
            min_index = i if prices[i]<prices[min_index] else min_index

    return res