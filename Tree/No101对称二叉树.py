


def isSymmetric(self, root: TreeNode) -> bool:
    return self.Iteration(root)


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
    