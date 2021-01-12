
# 由于有删除自己的情况，因此传入一个父节点已经记录左右子树关系的变量
def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
    def DFS(head, parent, d):
        if not head:
            return  

        DFS(head.left, head, 1)
        DFS(head.right, head, 0)
        if head.left == None and head.right == None and head.val == target:
            if d == 1:
                parent.left = None
            else:
                parent.right = None
            return


    dummy = TreeNode(-1)
    dummy.left = root
    DFS(root, dummy, 1)
    return dummy.left