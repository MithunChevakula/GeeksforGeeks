class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        return self.check_bst(root, float('-inf'), float('inf'))
        
        
    def check_bst(self, node, left_edge, right_edge):
        
        if not node: 
            return True
        
        if node.data <= left_edge:
            return False
        
        if node.data >= right_edge:
            return False
        
        
        return self.check_bst(node.left, left_edge, node.data) and self.check_bst(node.right, node.data, right_edge)