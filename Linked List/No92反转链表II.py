# 先遍历确定要反转的区间，以及区间的前置节点和后续节点
# 然后反转区间内的节点，最后再相互连接

def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    if head == None or head.next == None or m == n:
        return head
    
    # 这里有一个易错点在于：在反转函数中，我们在判断结束条件的时候需要注意区间内的尾节点的指向已经改变
    # 因此在while条件中，不能使用a!=t.next，因为t.next变了
    # 我们应该使用反转时的前置节点来判断，也就是p != t，因为t不会变
    def reverse(h, t):
        p = ListNode(None)
        a = h
        while p != t:
            n = a.next
            a.next = p
            p = a
            a = n
        return t,h

    start = ListNode(None)
    start.next = head

    front, begin, end, next = start, head, head, head.next
    cur,pre = head, start
    count = 1
    while count<=n:
        if count == m:
            front = pre
            begin = cur
        if count == n:
            end = cur
            next = end.next
        cur = cur.next
        pre = pre.next
        count += 1

    begin,end = reverse(begin, end)
    front.next = begin
    end.next = next
    
    return start.next