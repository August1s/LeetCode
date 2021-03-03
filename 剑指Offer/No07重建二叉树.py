

# 根据前序遍历和中序遍历递归构造二叉树
# 首先我们知道preorder[0]一定是根节点，因此我们可以通过遍历inorder找到中序遍历根节点的位置
# 这样我们就可以知道左右子树的长度,，然后递归构建

def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if preorder == [] or inorder == []:
        return 

    root = TreeNode(preorder[0])
    i = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1:i+1], inorder[:i])
    root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

    return root