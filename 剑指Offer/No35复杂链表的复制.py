

# 使用hashmap记住新老节点之间的对应关系，这样在构建random指向的时候比较方便

def copyRandomList(self, head: 'Node') -> 'Node':
    dic1 = {}
    dic2 = {}
    dummy = Node(-1)
    q = dummy
    p = head
    while p:
        q.next = Node(p.val)
        dic2[p] = q.next
        dic1[q.next] = p

        q = q.next
        p = p.next
    
    q = dummy.next
    while q:
        temp = dic1[q]
        if not temp.random:
            q.random = None
        else:
            q.random = dic2[temp.random]
        q = q.next
    return dummy.next