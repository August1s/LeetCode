    
'''
# 使用一个list暂存遍历结果
def hasCycle(self, head: ListNode) -> bool:
    if not head:
        return False
    L = [head]
    p = head
    while(p):
        p = p.next
        if p in L:
            return True
        else:
            L.append(p)
    return False 
'''

# 使用两个快慢指针，步长分别为一步和两步
# 如果链表存在环，快指针迟早会和慢指针相遇；如果不存在环，快指针最终会指向null
def hasCycle(self, head: ListNode) -> bool:
    if not head or not head.next:
        return False
    p = head
    q = head.next
    while(q.next and q.next.next):
        if p == q:
            return True
        else:
            p = p.next
            q = q.next.next
    return False

