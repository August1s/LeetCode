
# 我们可以使用快慢指针寻找中间结点
# 如果是正中间，快指针使用1步步长，慢指针使用2步步长
# 这样，在快指针到达链表末尾的时候，慢指针就刚好到一半位置
def middleNode(self, head: ListNode) -> ListNode:
    if head == None:
        return None
    
    p, q = head, head
    while q and q.next:
        p = p.next
        q = q.next.next
    
    return p