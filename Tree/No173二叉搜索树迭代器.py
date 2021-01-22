
# 很容易想到使用中序遍历进行迭代
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes = []

        def DFS(root):
            if not root: return
            DFS(root.left)
            self.nodes.append(root.val)
            DFS(root.right)

        DFS(root)
        self.index = 0

    def next(self) -> int:
        res = self.nodes[self.index]
        self.index += 1
        return res

    def hasNext(self) -> bool:
        if self.index == len(self.nodes):
            return False
        else:
            return True