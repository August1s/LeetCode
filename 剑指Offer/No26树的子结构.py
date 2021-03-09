
# 在子结构判定的过程使用后序遍历
# 但是在判定前需要先找判定位置再开始递归判定

def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
    if not B:
        return False

    def DFS(node1, node2):
        if not node1 and not node2:
            return True
        elif (not node1 and node2):
            return False
        elif (node1 and not node2):
            return True
        else:
            if node1.val == node2.val:
                l = DFS(node1.left, node2.left)
                r = DFS(node1.right, node2.right)
                return l and r
            else:
                return False


    def Search(node):
        if not node:
            return False
        if node.val==B.val:
            return DFS(node, B) or Search(node.left) or Search(node.right)
        else:
            return Search(node.left) or Search(node.right)

    return Search(A)