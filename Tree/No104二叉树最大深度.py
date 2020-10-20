


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root: TreeNode) -> int:
    #return Dfs(root)
    return Bfs(root)

'''
def Dfs(node):
    if not node.left and not node.right:
        return 0
    elif not node.left:
        return 1 + Dfs(node.right)
    elif not node.right:
        return 1 + Dfs(node.left)
    else:
        return 1 + max(Dfs(node.left), Dfs(node.right))
'''
'''
def Dfs(node):
    if not node:
        return 0
    else:
        return 1 + max(Dfs(node.left), Dfs(node.right))'''

def Bfs(node):
    if not node:
        return 0
    queue = [node]
    count = 0
    while queue != []: 
        layer = []
        while queue != []:
            n = queue.pop(0)
            if n.left:
                layer.append(n.left)
            if n.right:
                layer.append(n.right) 
        count += 1
        queue = layer
    return count
