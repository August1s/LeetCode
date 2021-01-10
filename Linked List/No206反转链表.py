
# 迭代法
# 使用pre记录前一个节点，使用cur记录当前节点
def reverseList(self, head: ListNode) -> ListNode:

    pre, cur = None, head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    return pre


# 利用栈
def reverseList(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    L = []
    while head:
        L.append(head)
        head = head.next

    newhead = L.pop()
    p = newhead
    p.next = None
    while L:
        temp = L.pop()
        p.next = temp
        temp.next = None
        p = temp

    return newhead