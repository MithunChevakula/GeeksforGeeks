#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        n=len(arr)
        res=[]
        total=1
        for i in arr:
            if i!=0:
                total=total*i
        if arr.count(0)>1:
            return [0]*n
        elif arr.count(0)==1:
            idx=arr.index(0)
            arr.remove(0)
            res=[0]*(n-1)
            res.insert(idx,total)
        else:
            for i in arr:
                res.append(total//i)
        return res