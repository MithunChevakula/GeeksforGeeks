class Solution:
    def farMin(self, arr):
        # Code Here
        maxi=-1
        ans=[-1]*(len(arr))
        for val,ind in sorted((arr[i],i) for i in range(len(arr))):
            if ind<maxi:
                ans[ind]=maxi
            maxi=max(ind,maxi)
        return ans