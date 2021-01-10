
'''
# 一个简单的做法是将访问过的节点存储下来
def detectCycle(self, head: ListNode) -> ListNode:
    
    if not head or not head.next:
        return None
    
    L = []
    p = head
    while p:
        if p in L:
            return p
            break
        L.append(p)
        pre = p
        p = p.next

    return None
'''

# 利用快慢指针的距离关系
# 首先我们假设从表头开始，走距离a到入环点，走距离b到快慢指针的第一次相交点，再走c到入环点
# 我们假设快指针走了n圈，那么快指针走过的长度是：a + n*(b+c) + b
# 相对的 慢指针走过的长度是：a+b
# 因此根据两个指针的步长可以得到 a + n*(b+c) + b = 2*(a+b)，解得 a = c + (n-1)*(b+c)
# a是表头到入环点，c是相遇点到入环点，(n-1)*(b+c)是n-1个整圈
# 这样我们可以再安排一次双指针，P从表头开始走，Q从相交点开始走，这样Q在走了n-1圈后，在第n圈就会刚好和P在入环点相遇
def detectCycle(self, head: ListNode) -> ListNode:
    
    fast, slow = head, head
    while True:
        if not (fast and fast.next): 
            return None
        fast, slow = fast.next.next, slow.next
        if fast == slow: 
            break
    
    fast = head
    while fast != slow:
        fast, slow = fast.next, slow.next
    return fast