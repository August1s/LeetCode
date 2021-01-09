# 画图
# 将分隔位后的节点插入到分隔位前
def partition(self, head: ListNode, x: int) -> ListNode:
    if head == None or head.next == None:
        return head
    
    start = ListNode(None)
    start.next = head

    p, div = start, head
    while div and div.val < x:
        div = div.next
        p = p.next
    if not div:
        return head
    
    q, cur = div, div.next
    while cur:
        if cur.val < x:
            q.next = cur.next
            p.next = cur
            cur.next = div

            p = cur
            cur = q.next
        else:
            q = q.next
            cur = cur.next

    return start.next