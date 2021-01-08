'''
# 使用一个list存储元素然后使用切片的暴力方法
def reverseList(self, head: ListNode) -> ListNode:

    pre, cur = None, head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    return pre
'''

# 递归解法
# 递归特性可以让我们实现链表的逆序遍历
# 我们可以使用一个全局变量记录正向遍历，利用递归反向遍历，然后判断回文
def isPalindrome(self, head: ListNode) -> bool:
    self.pre = head

    def rec_check(cur):
        if cur:
            if not rec_check(cur.next):
                return False
            if self.pre.val != cur.val:
                return False
            self.pre = self.pre.next
        return True

    return rec_check(head)