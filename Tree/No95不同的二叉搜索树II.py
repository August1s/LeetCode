

def generateTrees(self, n: int) -> List[TreeNode]:
    if not n:
        return []

    def Bulid(start, end):
        if start > end:
            return [None]
        tree = []
        for i in range(start, end+1):
            ls = Bulid(start, i-1)
            rs = Bulid(i+1, end)
            for l in ls:
                for r in rs:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    tree.append(node)
        print(tree)
        return tree

    return Bulid(1,n)