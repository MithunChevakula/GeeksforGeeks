class Solution:
    def leaders(self, arr):
        # code here
        suffix=arr[-1]
        res=[arr[-1],]
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>=arr[i+1] and arr[i]>=suffix:
                suffix=arr[i]
                res.append(suffix)
        return res[::-1]