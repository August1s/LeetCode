
# 这道题唯一注意的就是需要对头节点进行单独判定
# 节点删除需要上一个节点的位置，因此在循环中，头节点是不会被判断的，需要在最后判断一下
# 当然也可以使用一个哨兵节点
def removeElements(self, head: ListNode, val: int) -> ListNode:
    if head == None:
        return None

    p, q = head.next, head
    while p :
        if p.val == val:
            q.next = p.next
            p = p.next
        else:
            q = p
            p = p.next

    if head.val == val:
        head = head.next

    return head

'''
def removeElements(self, head: ListNode, val: int) -> ListNode:

    start = ListNode(None)
    start.next = head
    p,q = head, start
    while p :
        if p.val == val:
            q.next = p.next
            p = p.next
        else:
            q = p
            p = p.next


    return start.next
'''