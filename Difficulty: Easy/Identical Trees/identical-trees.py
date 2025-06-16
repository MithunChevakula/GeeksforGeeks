class Solution:
    #Function to check if two trees are identical.
    def is_BST(self, root, arr):
        if not root:
            return
        self.is_BST(root.left, arr)
        arr.append(root.data)
        self.is_BST(root.right, arr)
        return arr
        
    def isIdentical(self,r1, r2):
        # Code here
        return self.is_BST(r1, []) == self.is_BST(r2, [])