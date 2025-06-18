class Solution:
    def maxPathSum(self, root):
        def dfs(cur=root):
            if not cur:
                return 0,-float('inf')
            if not cur.left and not cur.right:
                return cur.data,-float('inf')
            l1,l2=dfs(cur.left)
            r1,r2=dfs(cur.right)
            if not cur.left:
                l1=l2=-float('inf')
            if not cur.right:
                r1=r2=-float('inf')
            return max(l1,r1)+cur.data,max(l2,r2,l1+r1+cur.data)
        ret=dfs()
        return ret[1] if ret[1]!=-float('inf') else ret[0]

