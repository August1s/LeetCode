

# 迭代法
# 使用对于两两一对的节点使用p，q表示，同时使用一个pre指向上一个节点
# 0 -> (0 -> 0) -> 0 -> ...
# pre   p    q
# 首先，需要将pre指向q，然后交换pq的位置，最后将下一次交换的pre设置为p   
def swapPairs(self, head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head

    start = ListNode(None)
    start.next = head

    pre,p = start,head
    while p and p.next:
        q = p.next
        
        pre.next = q
        p.next = q.next
        q.next = p

        pre = p
        p = p.next
    return start.next


# 递归
def swapPairs(self, head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head
    newhead = head.next
    head.next = self.swapPairs(newhead.next)
    newhead.next = head
    return newhead