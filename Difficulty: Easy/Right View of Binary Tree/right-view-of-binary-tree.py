'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        
        # code here
        res=[]
        if root==None:
            return res
        q=[]
        q.append(root)
        while q:
            temp=[]
            for i in range(len(q)):
                node=q.pop(0)
                temp.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
        l=[]    
        for i in res:
            l.append(i[-1])
        return l    