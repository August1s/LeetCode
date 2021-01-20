

# 涉及到求和，可以用DFS返回求和值
sum = 0
def findTilt(self, root: TreeNode) -> int:
    def DFS(head):
        if not head:
            return 0
        
        l = DFS(head.left)
        r = DFS(head.right)

        self.sum += abs(l-r)

        return head.val + l + r

    DFS(root)
    return self.sum