def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    count = 0
    p = list1
    pre1,next1 = None,None
    while p:
        if count+1 == a:
            pre1 = p
        if count == b:
            next1 = p.next
            break
        count += 1
        p = p.next

    trail = list2
    while trail.next:
        trail = trail.next

    pre1.next = list2
    trail.next = next1
    return list1