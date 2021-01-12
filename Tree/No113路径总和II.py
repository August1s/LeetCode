

def pathSum(self, root: TreeNode, Sum: int) -> List[List[int]]:
    res = []
    L = []

    def DFS(head):
        if not head:
            return 
        if not head.left and not head.right:
            if sum(L) + head.val == Sum:
                res.append(L + [head.val])
            return
                
        L.append(head.val)
        DFS(head.left)
        DFS(head.right)
        L.pop()

    DFS(root)
    return res