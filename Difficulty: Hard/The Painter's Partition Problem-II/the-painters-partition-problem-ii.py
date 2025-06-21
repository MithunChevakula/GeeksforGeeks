class Solution:
    def minTime (self, arr, k):
        #code here
        l,r=0,sum(arr)
        
        def helper(m):
            count=1
            cur=0
            for i in arr:
                if cur+i<=m:
                    cur+=i
                else:
                    count+=1
                    if count>k or i>m:
                        return 0
                    cur=i
            return 1    
        
        while l<=r:
            m=l+(r-l)//2
            if helper(m):
                ans=m
                r=m-1
            else:
                l=m+1
        return ans