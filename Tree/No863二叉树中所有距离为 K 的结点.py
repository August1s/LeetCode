
# 如果能够为树中的所有节点添加一个指向父节点的指针，那么求距离问题就可以转化为BFS求距离问题
# 不过需要注意的就是需要控制访问
# 这里我们使用一个DFS统计父节点，顺便初始化节点访问列表
def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
    
    parent = {} # 使用一个hashmap保存节点的父节点
    visted = {} # 使用一个hashmap记录节点是否访问
    def DFS(head):
        if not head:
            return

        visted[head] = False
        if head.left:
            parent[head.left] = head
        if head.right:
            parent[head.right] = head
        DFS(head.left)
        DFS(head.right)

    DFS(root)
    parent[root] = None

    queue = [target] 
    distance = 0
    while queue:
        if distance == K:
            break
        size = len(queue)
        for _ in range(size):
            node = queue.pop()
            if node.left != None and not visted[node.left]:
                queue.insert(0, node.left)
            if node.right != None and not visted[node.right]:
                queue.insert(0, node.right)
            if parent[node] != None and not visted[parent[node]]:
                queue.insert(0, parent[node])
            visted[node] = True
        distance += 1

    res = []   
    for n in queue:
        res.append(n.val)
    return res