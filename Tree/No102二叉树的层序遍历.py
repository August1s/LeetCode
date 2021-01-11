def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        size = len(queue)
        L = []
        for _ in range(size):
            node = queue.pop()
            L.append(node.val)
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        res.append(L)

    return res