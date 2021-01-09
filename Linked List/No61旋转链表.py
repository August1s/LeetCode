'''
# 首先计算长度，得出需要旋转的节点个数
# 然后使用快慢指针得到需要被移动到头节点位置的区间
def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if not head or not head.next:
        return head
    
    length = 0
    c = head
    while c:
        length += 1
        c = c.next
    k = k % length
    if k == 0:
        return head
    
    start = ListNode(None)
    start.next = head
    pre, p, q = start, head, head
    for i in range(k-1):
        q = q.next
    
    while q.next:
        p = p.next
        q = q.next
        pre = pre.next

    pre.next = None
    start.next = p
    q.next = head

    return start.next
'''

# 一个比较简单的方法是将这个链表看成一个环
# 通过在环上重新定义head和trail来完成旋转操作
def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if not head or not head.next:
        return head
    
    length = 1
    trail = head
    while trail.next:
        length += 1
        trail = trail.next
    k = k % length
    if k == 0:
        return head
    
    trail.next = head

    trail = head
    for i in range(length - k -1):
        trail = trail.next
    head = trail.next
    trail.next = None

    return head