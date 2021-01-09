
# 内置一个循环来判断重复元素的范围
def deleteDuplicates(self, head: ListNode) -> ListNode:
    start = ListNode(None)
    start.next = head

    pre, cur = start, head
    while cur:
        
        while cur.next:
            if cur.val != cur.next.val:
                break
            cur = cur.next

        if pre.next == cur:
            pre = cur
            cur = cur.next
        else:
            pre.next = cur.next
            cur = cur.next
    return start.next