def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
    
    def Build(preorder, postorder):
        if not preorder:
            return

        node = TreeNode(preorder[0])
        if len(preorder) == 1:
            return node
        i = postorder.index(preorder[1]) # 找到左右子树的分界点
        node.left = Build(preorder[1:i+2], postorder[:i+1])
        node.right = Build(preorder[i+2:], postorder[i+1:-1])

        return node

    return Build(pre, post)