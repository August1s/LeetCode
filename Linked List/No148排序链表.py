# 自底向下的归并排序
def sortList(self, head: ListNode) -> ListNode:
    
    dummy = ListNode(None)
    dummy.next = head

    length,p = 0,head
    while p :
        p = p.next
        length += 1

    i = 1   # 设定不同的分组长度i（1,2,4...），直到等于length为止
    while i<length:
        cur = dummy
        
        j=0 # 对组进行两两归并，j的循环步长应该是两个组，也就是2*i
        while j + i < length:
            
            left=right=cur.next # 寻找两个组的起点
            for k in range(i):
                if right:   # 值得注意的是，right的长度不一定等于i，有可能小于i
                    right = right.next

            # 归并过程
            l=r=0
            while l<i and r<i and right:    
                if left.val <= right.val:
                    cur.next = left
                    cur = left
                    left = left.next
                    l += 1
                else:
                    cur.next = right
                    cur = right
                    right = right.next
                    r += 1
            while l < i:
                cur.next = left
                cur = left
                left = left.next
                l += 1
            while r < i and right:
                cur.next = right
                cur = right
                right = right.next
                r += 1   

            cur.next = right    # 将cur移动到下一个组

            j += 2*i
        
        i *= 2

    return dummy.next