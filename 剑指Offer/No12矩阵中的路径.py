# def exist(self, board: List[List[str]], word: str) -> bool:
    # def DFS(path):
    #     if len(path) == len(word):
    #         return True

    #     else:
    #         lastPos = path[-1]
    #         res = False
    #         if lastPos[0]>0:
    #             curPos = (lastPos[0]-1, lastPos[1])
    #             if not (curPos in path) and board[curPos[0]][curPos[1]] == word[len(path)]:
    #                 res = res or DFS(path + [curPos])
    #         if lastPos[0]<len(board)-1:
    #             curPos = (lastPos[0]+1, lastPos[1])
    #             if not (curPos in path) and board[curPos[0]][curPos[1]] == word[len(path)]:
    #                 res = res or DFS(path + [curPos])
    #         if lastPos[1]>0:
    #             curPos = (lastPos[0], lastPos[1]-1)
    #             if not (curPos in path) and board[curPos[0]][curPos[1]] == word[len(path)]:
    #                 res = res or DFS(path + [curPos])
    #         if lastPos[1]<len(board[0])-1:
    #             curPos = (lastPos[0], lastPos[1]+1)
    #             if not (curPos in path) and board[curPos[0]][curPos[1]] == word[len(path)]:
    #                 res = res or DFS(path + [curPos])

    #         return res

    # r = False     
    # for i in range(len(board)):
    #     for j in range(len(board[0])):
    #         if r:
    #             return r
    #         if board[i][j] == word[0]:
    #             r = r or DFS([(i,j)])
    # return r

# 基本上的思路就是使用DFS找路径
# 这里有一个技巧是，通过改变board[i][j]为#来表示该路径已经被访问，而不用像上面那样再传一个记录的参数进去，判断也会更快

def exist(self, board: List[List[str]], word: str) -> bool:
    def DFS(i,j,index):
        if index == len(word):
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return False
        if board[i][j] != word[index]:
            return False
        else:
            board[i][j] = '#'
            res =  DFS(i-1,j,index+1) or DFS(i+1,j,index+1) or DFS(i,j+1,index+1) or DFS(i,j-1,index+1)
            board[i][j] = word[index]
            return res

    res = False
    for i in range(len(board)):
        for j in range(len(board[0])):
                res = res or DFS(i,j,0)
    return res