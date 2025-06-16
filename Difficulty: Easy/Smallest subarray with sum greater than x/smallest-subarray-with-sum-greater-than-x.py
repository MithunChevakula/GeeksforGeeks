class Solution:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here
        sum=0
        minl=len(arr)+1
        i=0
        for j in range(len(arr)):
            if sum<=x:
                sum+=arr[j]
            if sum>x:
                minl=min(minl,j-i+1)
                while sum>x and i<=j:
                    minl=min(minl,j-i+1)
                    sum-=arr[i]
                    i+=1
        if minl>len(arr):return 0
        else:
            return minl
        
