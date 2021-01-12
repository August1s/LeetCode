

# DFS,使用一个全局变量记录当前路径中的最大值
count = 0
pathmax = -99999
def goodNodes(self, root: TreeNode) -> int:
    
    def DFS(head):
        if not head:
            return 

        temp = self.pathmax
        if head.val >= self.pathmax: 
            self.pathmax = head.val
            self.count += 1
        DFS(head.left)
        DFS(head.right)
        self.pathmax = temp

    DFS(root)

    return self.count