#User function Template for python3

class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        #code here
        
        i=0
        j=m-1
        diff=float("inf")
        sum=0
        ans1=0
        ans2=0
        while i<n and j>=0:
            sum=arr[i]+brr[j]
            if abs(sum-x)<diff:
                diff=abs(sum-x)
                ans1=arr[i]
                ans2=brr[j]
            if sum<x:
                i+=1
            else:
                j-=1
        return [ans1,ans2]