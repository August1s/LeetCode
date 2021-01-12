def serialize(self, root):
    if not root:
        return root
    queue = [root]
    res = []

    def IsNone(l):
        for i in l:
            if i:
                return False
        return True        

    while queue:
        
        size = len(queue)
        if IsNone(queue[:size]):
            break

        for _ in range(size):
            node = queue.pop()
            if node:
                queue.insert(0, node.left)
                queue.insert(0, node.right)
                res.append(node.val)
            else:
                res.append(None)

    return res
    

def deserialize(self, data):
    
    if not data:
        return None
    
    rval = data.pop(0)
    root = TreeNode(rval)
    L = [root]

    while data:
        cache = []
        for node in L:
            if data == []:
                break
            if not node:
                continue
            #print(data)
            lval = data.pop(0)
            if not lval == None:
                node.left = TreeNode(lval)
                cache.append(node.left)
            rval = data.pop(0)
            if not rval == None:
                node.right = TreeNode(rval)
                cache.append(node.right)
        L = cache

    return root


