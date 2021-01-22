# 利用二叉搜索树的中序遍历性质
def isValidBST(self, root: TreeNode) -> bool:
    if not root:
        return True
    if not root.left and not root.right:
        return True
    
    nodes = []
    def DFS(head):
        if not head:
            return
        DFS(head.left)
        nodes.append(head.val)
        DFS(head.right)

    DFS(root)
    for i in range(1, len(nodes)):
        if nodes[i]<=nodes[i-1]:
            return False

    return True
