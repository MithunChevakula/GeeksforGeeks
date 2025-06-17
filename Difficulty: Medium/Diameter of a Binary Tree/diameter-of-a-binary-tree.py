class Solution:
    def height(self, root, diff):
        if not root: return -1
        l = 1 + self.height(root.left, diff)
        r = 1 + self.height(root.right, diff)
        diff[0] = max(diff[0], l + r)
        return max(l,r)
        
    def diameter(self, root):
        diff = [0]
        self.height(root, diff)
        return diff[0]