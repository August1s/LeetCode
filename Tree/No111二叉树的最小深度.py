# 使用BFS是最好写的，找到叶子节点直接返回深度即可
def minDepth(self, root: TreeNode) -> int:
    if not root: return 0     

    queue = [root]
    depth = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.pop()
            if not node.left and not node.right:
                return depth+1
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        depth += 1

    return depth