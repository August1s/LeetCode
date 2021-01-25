
# 右视图元素即为层序遍历时每一层的最后一个元素
def rightSideView(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        size = len(queue)
        temp = []
        for i in range(size):
            node = queue.pop()
            temp.append(node.val)
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        if temp:
            res.append(temp[-1])

    return res