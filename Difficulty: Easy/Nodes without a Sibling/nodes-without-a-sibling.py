'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def noSibling(root):
    # code here
    if not root:
        return 0
    queue=[]
    res=[]
    
    queue.append(root)
    while len(queue)>0:
        node=queue.pop(0)

#Check for nodes with no siblings
        if node.left is not None and node.right is None:
            left=node.left
            res.append(left.data)
        elif node.left is None and node.right is not None:
            right=node.right
            res.append(right.data)

#Level Order Traversal
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    res.sort()
    return res if len(res)>0 else [-1]