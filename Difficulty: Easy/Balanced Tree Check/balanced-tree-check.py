class Solution:
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right))+1
            
    def isBalanced(self,root):
        if root == None:
            return True
        if (abs(self.height(root.left)-self.height(root.right))<=1) and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False