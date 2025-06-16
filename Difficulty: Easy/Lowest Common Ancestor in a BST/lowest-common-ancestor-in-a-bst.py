'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def LCA(self, root, n1, n2):
        # your code here
        low=min(n1.data,n2.data)
        high=max(n1.data,n2.data)
        while True:
            if root.data<low:
                root=root.right
            elif high<root.data:
                root=root.left
            else:
                return root
        
    