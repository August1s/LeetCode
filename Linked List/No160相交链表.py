'''
# 首先计算两个链表的长度差，然后根据长度差同时遍历两个链表
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    p, q = headA, headB
    lenA, lenB = 0, 0
    while(p):
        lenA += 1
        p = p.next
    while(q):
        lenB += 1
        q = q.next

    if lenA > lenB:
        count = lenA - lenB
        while count > 0:
            headA = headA.next
            count -= 1
    else:
        count = lenB - lenA
        while count > 0:
            headB = headB.next
            count -= 1
    
    while headA and headB:
        if headA == headB:
            return headA
        else:
            headA = headA.next
            headB = headB.next
    return None
'''
 
 # 对于两个长度不同的链表，我们可以在遍历其中一个链表的尾节点后，紧接着遍历另一个链表的头节点
 # 因为 先A后B 的长度和 先B后A 的遍历长度是一样的，这样就消除了长度差
 # 因此如果存在交点，则两个遍历的在遍历到交点处时，可以用判断检测出
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    p, q = headA, headB
    while p != q:
        p = p.next if p else headB
        q = q.next if q else headA
    return p