
# 使用一个hash维护新老链表的节点的关系，然后根据老链表的random在hash中寻找新链表对应的random
def copyRandomList(self, head: 'Node') -> 'Node':
    if not head:
        return None

    p = head
    newhead = Node(0)
    pre = newhead
    while p:
        copy = Node(p.val)
        pre.next = copy

        pre = pre.next
        p = p.next
    
    newhead = newhead.next

    hashmap = {}
    p = head
    np = newhead
    while p:
        hashmap[p] = np
        p = p.next
        np = np.next

    p = head
    np = newhead
    while p:
        if p.random:
            np.random = hashmap[p.random]
        p = p.next
        np = np.next

    return newhead