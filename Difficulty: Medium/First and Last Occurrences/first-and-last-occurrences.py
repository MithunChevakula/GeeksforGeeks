#User function Template for python3


class Solution:
    def find(self, arr, x):
        
        # code here
        n = len(arr)
        L = []
        for i in range(n):
            if arr[i]==x:
                L.append(i)
            if arr[i]>x:
                break
        if L == []:
            return -1,-1
        return L[0],L[-1]