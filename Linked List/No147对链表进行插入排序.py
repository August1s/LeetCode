def insertionSortList(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    dummy = ListNode(None)
    dummy.next = head

    pre,cur = head, head.next
    while cur:
        next = cur.next

        p = dummy.next
        q = dummy
        while p != cur:
            if p.val >= cur.val:
                pre.next = next
                cur.next = p
                q.next = cur
                break
            else:
                q = p
                p = p.next

        if p == cur:
            pre = cur
            cur = next
        else:
            cur = next

    return dummy.next