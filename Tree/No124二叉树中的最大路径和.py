    
    

maxsum = -999999
def maxPathSum(self, root: TreeNode) -> int:
    def DFS(head):
        if not head:
            return 0

        l = DFS(head.left)
        r = DFS(head.right)
        # 最大路径和在这里的定义是计算左右的路径的和，因此计算路径和的时候使用 max(l, 0) + max(r, 0) + head.val
        self.maxsum = max(self.maxsum, max(l, 0) + max(r, 0) + head.val)

        return max(l, r, 0) + head.val  # 构造路径和时候是单边选择，所以在左，右和不选 三个选项中选一个

    DFS(root)
    return self.maxsum