



# 简单思路是先存到一个数组中然后数组逆序

def reversePrint(self, head: ListNode) -> List[int]:
    L = []
    p = head
    while p:
        L.append(p.val)
        p = p.next
    return L[::-1]



# 如果使用先序遍历的递归的话也可以实现逆序

def reversePrint(self, head: ListNode) -> List[int]:
    L = []

    def DFS(node):
        if not node:
            return
        DFS(node.next)
        L.append(node.val)
        
    DFS(head)
    return L