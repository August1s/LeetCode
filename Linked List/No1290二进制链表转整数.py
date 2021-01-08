
# 一个比较容易想到的方法是先变为string再转为int
def getDecimalValue(self, head: ListNode) -> int:
    s = ""
    while head:
        s += str(head.val)
        head = head.next
    return int(s, 2)


# 递归可以反向遍历链表，因此可以使用
def getDecimalValue(self, head: ListNode) -> int:
    self.c = -1
    
    def rec(cur):
        if cur == None:
            return 0
        if cur.val == 1:
            num = rec(cur.next)
            self.c += 1
            return 2**self.c + num
        elif cur.val == 0:
            num = rec(cur.next)
            self.c += 1
            return num
    
    return rec(head)

# 最好的方法还是使用二进制转十进制本身的定义
def getDecimalValue(self, head: ListNode) -> int:
    num, cur = 0, head
    while cur:
        num = 2 * num + cur.val
        cur = cur.next
    return num