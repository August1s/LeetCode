
# 首先使用双指针确定需要重排的元素
# 然后借助了一个栈实现了逆序
# 最后扎入到之前的链表
def reorderList(self, head: ListNode) -> None:
    if not head or not head.next:
        return

    L = []
    p = q = head.next
    while(q.next and q.next.next):
        p = p.next
        q = q.next.next

    newtrail = p
    p = p.next
    while p:
        L.append(p)
        p = p.next

    newtrail.next = None
    p = head
    while L:
        temp = L.pop()
        temp.next = p.next
        p.next = temp
        p = p.next.next


# 当然也可以使用迭代法来逆序链表