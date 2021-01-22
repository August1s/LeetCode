
# 从根节点开始遍历
# 如果p,q均小于根节点，说明公共祖先在根节点左子树中
# 如果p,q均大于根节点，说明公共祖先在根节点右子树中
# 如果pq一个大于根节点，一个小于，说明当前节点就是它们的公共祖先
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def DFS(head):
        if head.val>p.val and head.val>q.val:
            return DFS(head.left)
        elif head.val<p.val and head.val<q.val:
            return DFS(head.right)
        else:
            return head
    return DFS(root)