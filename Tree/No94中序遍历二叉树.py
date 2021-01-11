
# 递归
def inorderTraversal(self, root: TreeNode) -> List[int]:
    L = []

    def DFS(head):
        if not head:
            return
        DFS(head.left)
        L.append(head.val)
        DFS(head.right)

    DFS(root)
    return L


# 使用“双色标记法”的迭代
# 使用一个栈记录节点之间的位置关系
def inorderTraversal(self, root: TreeNode) -> List[int]:
    L = []
    stack = [(0, root)]

    while stack:
        tag,node = stack.pop()
        if not node:
            continue
        if tag == 0:
            stack.append((0, node.right))
            stack.append((1, node))
            stack.append((0, node.left))
        else:
            L.append(node.val)

    return L