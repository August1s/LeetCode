
# 计算左右子树高度差
# 如果左右子树中存在不平衡，那么这个树也不平衡
def isBalanced(self, root: TreeNode) -> bool:
    def DFS(head):
        if not head:
            return (0, True)
        if not head.left and not head.right:
            return (1, True)
        
        lh, lb = DFS(head.left)
        rh, rb = DFS(head.right)
        h = max(lh,rh)+1
        if abs(lh-rh)<=1 and lb and rb:
            return(h, True)
        else:
            return(h, False)

    _, res = DFS(root)
    return res