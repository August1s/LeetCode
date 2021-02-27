
# dp[i][j]记录了第i行j列的节点的
def minimumTotal(self, triangle: List[List[int]]) -> int:
    n = len(triangle)
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif j == len(triangle[i])-1:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j-1])

    return min(dp[-1])


# 优化主要是空间进行优化
# 一个方案是使用两个滚动数组记录结果
def minimumTotal(self, triangle: List[List[int]]) -> int:
    n = len(triangle)
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                dp[i%2][j] = triangle[i][j] + dp[(i-1)%2][j]
            elif j == i:
                dp[i%2][j] = triangle[i][j] + dp[(i-1)%2][j-1]
            else:
                dp[i%2][j] = triangle[i][j] + min(dp[(i-1)%2][j], dp[(i-1)%2][j-1])
    
    return min(dp[(n-1)%2])

# 还有一个优化方法是使用原三角形数组来记录dp
def minimumTotal(self, triangle: List[List[int]]) -> int:
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])

    return min(triangle[-1])
