
# 递归寻找数组中间位置为根节点
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    def DFS(start, end):
        if start == end:
            return None

        
        index = (start+end)//2
        root = TreeNode(nums[index])
        root.left = DFS(start, index)
        root.right = DFS(index+1, end)
        return root

    return DFS(0, len(nums))