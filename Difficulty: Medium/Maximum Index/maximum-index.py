#User function Template for python3
class Solution:
    def maxIndexDiff(self, arr):
        # code here
        n = len(arr)
        maxElem = -1
        ans = 0
        rightMax = [0] * n
        for i in range(n-1, -1, -1):
            maxElem = max(maxElem, arr[i])
            rightMax[i] = maxElem
    
        i = j = 0
    
        while i < n and j < n:
            if rightMax[j] >= arr[i]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
        
        return ans