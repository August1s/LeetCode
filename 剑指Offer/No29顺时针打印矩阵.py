
# 模拟顺时针的遍历过程
# 使用一个数组记录访问情况，使用一个变量记录遍历方向

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    if matrix==[] or matrix==[[]]:
        return []
    m,n = len(matrix),len(matrix[0])
    visted = [[False]*n for _ in range(m)]
    res = []
    direction = {"right":"down", "down":"left", "left":"up", "up":"right"}

    i,j = 0,0
    d = "right"
    while True:
        res.append(matrix[i][j])
        visted[i][j] = True
        if len(res)==m*n:
            break
        if d=="right":
            if j+1==n or visted[i][j+1]:
                d = direction[d]
                i,j = i+1,j
            else:
                i,j = i, j+1
        elif d=="down":
            if i+1==m or visted[i+1][j]:
                d = direction[d]
                i,j = i,j-1
            else:
                i,j = i+1,j
        elif d=="left":
            if j==0 or visted[i][j-1]:
                d = direction[d]
                i,j = i-1,j
            else:
                i,j = i,j-1
        else:
            if visted[i-1][j]:
                d = direction[d]
                i,j = i,j+1
            else:
                i,j = i-1,j

    return res