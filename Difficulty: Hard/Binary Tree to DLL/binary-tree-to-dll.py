class Solution:
    def Inorder(self, root, l):
        if root is not None:
            self.Inorder(root.left, l)
            l.append(root.data)
            self.Inorder(root.right, l)
        
        return l
    
    
    def bToDLL(self,root):
        l = []
        l = self.Inorder(root, l)
        
        n = len(l)
        node = Node(l[n-1])
        
        for i in range(n-2, -1, -1):
            p = Node(l[i])
            
            p.right = node
            node.left = p
            node = p
        
        return node