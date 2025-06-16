#User function Template for python3

class Solution:

    def findMinDiff(self, arr,M):

        # code here
        arr.sort()
        i = 0
        j = M - 1 
        min_diff = float('inf')
        while j < len(arr):
            diff = arr[j] - arr[i]
            min_diff = min(min_diff, diff)
            i += 1
            j += 1
        return min_diff