
# 本质是减去和为0的子树
# 根节点也可以被减，所以使用一个虚拟节点
def pruneTree(self, root: TreeNode) -> TreeNode:
    def DFS(head):
        if not head:
            return 0
        
        l = DFS(head.left)
        r = DFS(head.right)

        if l == 0:
            head.left = None
        if r == 0:
            head.right = None
        return head.val + l + r

    dummy = TreeNode(-1)
    dummy.left = root
    DFS(dummy)
    return dummy.left