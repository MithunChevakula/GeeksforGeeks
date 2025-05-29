'''
class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def sumOfLongRootToLeafPath(self, root):
        #code here
        ans = [0, 0]
        self.dfs(root, ans, 0, 0)
        return ans[1]
    
    def dfs(self, root, ans, currSum, pathLength):
        if root == None:
            return
        
        if root.left == None and root.right == None:
            if pathLength + 1 > ans[0]:
                ans[0], ans[1] = pathLength + 1, root.data + currSum
            elif pathLength + 1 == ans[0]:
                ans[0], ans[1] = pathLength + 1, max(ans[1], root.data + currSum)
                
            return
        
        self.dfs(root.left, ans, currSum + root.data, pathLength + 1)
        self.dfs(root.right, ans, currSum + root.data, pathLength + 1)