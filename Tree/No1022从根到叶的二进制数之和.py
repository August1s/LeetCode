
# DFS，使用参数传递路径
# 一个优化方法是将字符串转换变成乘法
Sum = 0
def sumRootToLeaf(self, root: TreeNode) -> int:
    def DFS(head, path):
        if not head:
            return
        if not head.left and not head.right:
            self.Sum += int(path+str(head.val), 2)
        else:
            path += str(head.val)
            DFS(head.left, path)
            DFS(head.right, path)

    DFS(root,"")
    return self.Sum