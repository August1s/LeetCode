
# 思路就是遍历网格中满足要求的点，使用DFS和BFS都行

def movingCount(self, m: int, n: int, k: int) -> int:
    IsIn = [[0]*n for _ in range(m)]

    def DFS(i, j):
        if i<0 or i>=m or j<0 or j>=n:
            return
        if (i//10)+(i%10)+(j//10)+(j%10)>k:
            return
        if IsIn[i][j] == 1:
            return
        else:
            IsIn[i][j] = 1
            DFS(i-1,j)
            DFS(i+1,j)
            DFS(i,j-1)
            DFS(i,j+1)

    DFS(0,0)
    count = 0
    for i in range(m):
        for j in range(n):
            if IsIn[i][j]==1:
                count += 1

    return count

# 虽然题目中说了可以上下左右移动，但是实际上由于是从(0, 0)开始，我们完全可以只进行向右和向下的移动，这样使用BFS更加方便
# 
# 但是不知道为什么，超时了。。。
#
# def movingCount(self, m: int, n: int, k: int) -> int:
#     IsIn = [[0]*n for _ in range(m)]

#     IsIn[0][0] = 1
#     queue = [(0,0)]
#     while queue != []:
#         i,j = queue.pop(0)
#         if i<m-1 and ((i+1)//10)+((i+1)%10)+(j//10)+(j%10)<=k:
#             queue.append((i+1, j))
#             IsIn[i+1][j] = 1
#         if j<n-1 and (i//10)+(i%10)+((j+1)//10)+((j+1)%10)<=k:
#             queue.append((i, j+1))
#             IsIn[i][j+1] = 1

#     count = 0
#     for i in range(m):
#         for j in range(n):
#             if IsIn[i][j]==1:
#                 count += 1
#     return count