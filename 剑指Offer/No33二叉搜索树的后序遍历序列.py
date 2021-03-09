
# 首先根据后序遍历可以确定最后一个元素一定是根节点
# 然后根据搜索树的性质可以找到左右子树的分界点，也就是第一个大于根节点的数
# 左右子树划分以后，如果右子树存在小于根节点的值的话，直接return False
# 否则对子树进行递归

def verifyPostorder(self, postorder: List[int]) -> bool:
    def DFS(L):
        if L==[] or len(L)==1:
            return True

        n = L[-1]
        index = len(L)-1
        for i in range(len(L)-1):
            if L[i]>n:
                index = i
                break
        left = L[:index]
        right = L[index:len(L)-1]

        for i in right:
            if i<n:
                return False
        return DFS(left) and DFS(right)
            
    return DFS(postorder)