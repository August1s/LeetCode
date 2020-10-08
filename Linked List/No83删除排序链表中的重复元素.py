from No2两数相加 import ListNode
from No2两数相加 import LinkList


def deleteDuplicates(head: ListNode) -> ListNode:
    if head == None:
        return head
    p = head
    q = p.next
    while True:
        if q == None:
            return head
        if q.val == p.val:
            p.next = q.next
            q = p.next
        else:
            p = p.next
            q = q.next