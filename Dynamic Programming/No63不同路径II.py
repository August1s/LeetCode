def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    dp = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] ==1 :
                dp[i][j] = -1
                continue

            if i == 0:
                if dp[i][j-1] == -1:    
                    dp[i][j] = -1
                else:   
                    dp[i][j] = 1

            if j == 0:
                if dp[i-1][j] == -1:   
                    dp[i][j] = -1
                else:
                    dp[i][j] = 1

            if i!=0 and j!=0:
                dp[i][j] = max(dp[i-1][j], 0) + max(dp[i][j-1], 0)

    return max(dp[-1][-1], 0)