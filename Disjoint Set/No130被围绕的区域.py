
# 不知道为什么超时了
# 使用一个dummy，将所有边缘节点和dummy节点做Union操作
# 这样的话，我们可以对每一个点，使用Find判断它们是否在一个集合中

def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def Find(x,p):
            x_root = x
            while p[x_root]!=-1:
                x_root = p[x_root]
            return x_root

        def Union(x,y,p):
            x_root, y_root = Find(x,p), Find(y,p)
            if x_root!=y_root:
                p[y_root] = x_root


        m = len(board)
        n = len(board[0])
    
        dummy = (-1,-1)
        
        parent = {}
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    parent[(i, j)] = -1
        parent[dummy] = -1

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' :
                    if j>0 and board[i][j-1] == 'O':
                        Union((i,j), (i,j-1), parent)
                    if i>0 and board[i-1][j] == 'O':
                        Union((i,j), (i-1,j), parent)
                    if i==0 or j==0 or i==m-1 or j==n-1:
                        Union((i,j), dummy, parent)

        # print(parent)
        # print(edgePoints)
        for key,_ in parent.items():
            if key!=dummy and Find(key,parent) != Find(dummy, parent):
                board[key[0]][key[1]] = 'X'