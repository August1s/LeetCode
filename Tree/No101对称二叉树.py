


def isSymmetric(self, root: TreeNode) -> bool:
    if not root:    return True
    #return self.Iteration(root)
    return Dfs(root.left, root.right)

''' 
def Iteration(self, rootnode: TreeNode) -> bool:
    Queue = [rootnode]
    while(True):
        if self.IsNull(Queue):
            return True
        Valbuffer = self.GetValBuffer(Queue)
        if Valbuffer != Valbuffer[::-1]:
            return False
        else:
            Nodebuffer = []
            for node in Queue:
                if node != None:
                    Nodebuffer.append(node.left)
                    Nodebuffer.append(node.right)
                else:
                    Nodebuffer.append(None)
                    Nodebuffer.append(None)

            Queue = Nodebuffer

def GetValBuffer(self, L):
    buffer = []
    for i in L:
        if i == None:
            buffer.append(None)
        else:
            buffer.append(i.val)
    return buffer

def IsNull(self, L):
    for i in L:
        if i != None: return False
    return True
'''
'''
# 递归比较左子树和右子树
# 递归终止条件：两个节点都为空，两个节点一个为空，两个节点不相等
def Dfs(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.val != right.val:
        return False
    return Dfs(left.left, right.right) and Dfs(left.right, right.left)
'''

# 队列不需要储存所有的节点，可以修改一些节点入队列的顺序
# 除根节点外，队列入队可以按照左子树的左节点+右子树的右节点，和，左子树的右节点+右子树左节点的顺序入队，然后两两比较
# 每次pop两个节点进行比较，然后将他们对应的子节点加入队列
def IterationQueue(root):
    if not root.left and not root.right:
        return True
    queue = [root.left, root.right]
    while(queue != []):
        left = queue.pop(0)
        right = queue.pop(0)
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)
    return True
        
