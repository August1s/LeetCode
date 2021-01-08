
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