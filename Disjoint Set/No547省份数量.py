def findCircleNum(self, isConnected: List[List[int]]) -> int:
    def Find(x, p):
        x_root = x
        while p[x_root]!=-1:
            x_root = p[x_root]
        return x_root

    def Union(x, y, p):
        x_root = Find(x, p)
        y_root = Find(y, p)
        if x_root!=y_root:
            p[y_root] = x_root

    n = len(isConnected)
    p = [-1]*n

    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if isConnected[i][j] == 1:
                Union(i, j, p)
        #print(p)

    res = 0
    for x in p:
        if x==-1:
            res += 1
    return res