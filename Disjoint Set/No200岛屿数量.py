
# 连通性问题的一个直接的解决方法是并查集

def numIslands(self, grid: List[List[str]]) -> int:
    def Find(x, p):
        x_root = x
        while p[x_root]!=-1:
            x_root = p[x_root]
        return x_root
    
    def Union(x:tuple, y:tuple, p:dict):
        x_root, y_root = Find(x,p), Find(y,p)
        if x_root != y_root:
            p[y_root] = x_root
    
    m, n = len(grid), len(grid[0])

    parent = {}

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                parent[(i,j)] = -1
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                if i>0 and grid[i-1][j]=='1':
                    Union((i-1,j), (i,j), parent)
                if j>0 and grid[i][j-1]=='1':
                    Union((i,j-1), (i,j), parent)   
    
    res = 0
    for _, item in parent.items():
        if item==-1:
            res += 1

    return res