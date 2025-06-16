#User function Template for python3
class Solution:
    def findKRotation(self, arr):
        # code here
        ans=[]
        for i in range(len(arr)):
            ans.append(arr[i])
        arr.sort()
        return ans.index(arr[0])