
# 求最大宽度依然使用层序遍历
# 由于两端点之间的空节点也算宽度，因此我们需要使用完全二叉树的编号性质来计算同一层的宽度
def widthOfBinaryTree(self, root: TreeNode) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    
    queue = [(root, 1)]
    depth, curdepth, maxwidth = -1,0,0
    while queue:
        size = len(queue)

        mostleft = 0    # 使用一个变量记录每一层中最左边节点的编号
        for _ in range(size):
            node, pos = queue.pop()
            if not node:    
                continue
            queue.insert(0, (node.left, pos*2))
            queue.insert(0, (node.right, pos*2+1))
            
            if depth != curdepth:   # 用深度变化判断节点知否为最左边节点

                depth = curdepth
                mostleft = pos

            maxwidth = max(maxwidth, pos-mostleft + 1)  # 根据编号来求解宽度

        curdepth += 1

    return maxwidth