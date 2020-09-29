


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

