class Solution:
    def findMedian(self, root):
        tmp=[]
        def dfs(cur=root):
            nonlocal tmp
            if not cur:
                return
            dfs(cur.left)
            tmp.append(cur.data)
            dfs(cur.right)
        dfs()
        return tmp[(len(tmp)-1)//2]