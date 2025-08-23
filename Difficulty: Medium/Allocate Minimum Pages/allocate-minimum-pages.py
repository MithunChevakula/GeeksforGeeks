class Solution:
    def findPages(self, arr, k):
        # code here
        # binary search
        
        def func(mid,k):
            s=0
            i=0
            while i<len(arr) and k>0:
                if s+arr[i]<=mid:
                    s+=arr[i]
                else:
                    k-=1
                    s=arr[i]
                i+=1
            if i<len(arr):
                return False
            return k!=0
            
        if len(arr)<k:
            return -1
            
        low=max(arr)
        high=sum(arr)
        
        while low<=high:
            mid=(low+high)//2
            val=func(mid,k)
            if val:
                high=mid-1
            else:
                low=mid+1
                
        return low
        
        