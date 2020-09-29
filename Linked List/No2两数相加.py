

class ListNode:     
    def __init__(self, x):
        self.value = x
        self.next = None


class LinkList:
    def __init__(self): # 头结点
        self.next = None
        self.trail = None # 尾插方便一点，不然append()要遍历
        self.length = 0    

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def append(self, item):
        node= ListNode(item)
        if self.next == None:
            self.next = node
        if self.trail == None:
            self.trail = node
        else:
            self.trail.next = node
            self.trail = node
        self.length += 1

    def insert(self, index, item):
        if self.isEmpty() or index < 0 or index > self.length:
            print('error')
            return 
        in_node = ListNode(item)
        pnode = self # 头指针
        count = 0
        while True:
            if count == index:
                in_node.next = pnode.next
                pnode.next = in_node
                self.length += 1
                return
            count += 1
            pnode = pnode.next

    def delete(self, index):
        if self.isEmpty() or index < 0 or index > self.length:
            print('error')
            return 
        pnode = self 
        count = 0
        while True:
            if count == index:
                pnode.next = pnode.next.next
                self.length -= 1
                return
            count += 1
            pnode = pnode.next

    def nodePrint(self):
        nstr = ""
        pnode = self.next
        nstr = nstr + str(pnode.value)

        while pnode.next!=None:
            pnode = pnode.next
            nstr = nstr + '->' + str(pnode.value)
        print(nstr)


# leetcode 部分
##################################################################
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:

    l3 = ListNode(0) # 头结点
    c=0 # 进位
    result = l3
    while True:
        if l1==None and l2 == None:
            break

        p = l1.value if l1 else 0
        q = l2.value if l2 else 0

        value = p+q+c
        c = value//10
        result.next = ListNode(value%10)
        result = result.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if c!=0:
        result.next = ListNode(c)
    return l3.next
##################################################################
        




'''
L1 = LinkList()
print(L1.isEmpty())

L2 = LinkList()
L2.append(7)
L2.append(3)
L2.nodePrint()
L2.insert(2,2)
L2.nodePrint()
L2.delete(4)
L2.nodePrint()
print(L2.length)

L3 = LinkList()
L3.next = addTwoNumbers(L1.next,L2.next)'''
