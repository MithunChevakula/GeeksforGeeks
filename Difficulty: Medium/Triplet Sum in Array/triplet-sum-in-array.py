class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        n=len(arr)
        arr.sort()
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                sum=arr[i]+arr[l]+arr[r]
                if sum==target:
                    return True
                if sum<target:
                    l+=1
                else:
                    r-=1
        return False
            