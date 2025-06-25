# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findLCA(self, root, a, b):
        """Finds the Lowest Common Ancestor (LCA) of nodes a and b."""
        if not root or root.data == a or root.data == b:
            return root
        
        left = self.findLCA(root.left, a, b)
        right = self.findLCA(root.right, a, b)
        
        if left and right:
            return root  # If a and b are found in different subtrees, root is the LCA
        
        return left if left else right  # Return the non-null subtree
    
    def findLevel(self, root, target, level):
        """Finds the level (depth) of target node from the given root."""
        if not root:
            return -1
        if root.data == target:
            return level
        
        left = self.findLevel(root.left, target, level + 1)
        if left != -1:
            return left
        
        return self.findLevel(root.right, target, level + 1)

    def findDist(self, root, a, b):
        """Finds the minimum distance between nodes a and b."""
        lca = self.findLCA(root, a, b)
        distA = self.findLevel(lca, a, 0)
        distB = self.findLevel(lca, b, 0)
        return distA + distB