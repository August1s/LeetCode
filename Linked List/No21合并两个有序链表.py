


'''
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    l3 = ListNode(None)
    head = l3
    
    while l2 != None and l1 != None:
        if l1.value <= l2.value:
            l3.next = ListNode(l1.value)
            l3 = l3.next
            l1 = l1.next
        else:
            l3.next = ListNode(l2.value)
            l3 = l3.next
            l2 = l2.next
    if l2 == None:
        l3.next = l1
    else:
        l3.next = l2 

    return head.next'''

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # 递归解法
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2


# 在改变原链表基础上的迭代法
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    start = ListNode()
    start.next = l1
    cur = start
    while True:
        if l1 and l2:
            if l1.val >= l2.val:
                cur.next = l2
                cur = l2
                l2 = l2.next
            else:
                cur.next = l1
                cur = l1
                l1 = l1.next

        elif l1 and not l2:
            cur.next = l1
            return start.next
        elif l2 and not l1:
            cur.next = l2
            return start.next
        else:
            return start.next
