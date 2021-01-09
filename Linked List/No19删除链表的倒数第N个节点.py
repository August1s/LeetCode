
# 使用快慢指针法
# 如果要求倒数第N个节点，我们只需要保证快指针和慢指针之间的差值为N
# 这可以通过让快指针提前走N步得到
# 为了处理删除头节点的情况，可以使用一个哨兵节点
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    
    start = ListNode(None)
    start.next = head

    pre = start
    p = q = head
    for i in range(0, n):
        q = q.next
    
    while q:
        pre = p
        p = p.next
        q = q.next

    pre.next = p.next

    return start.next


