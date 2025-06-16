class Solution:
    def transitionPoint(self, arr): 
        # Code here
        if 0 not in arr:
            return 0
        elif 1 not in arr:
            return -1
            
        for i in range(1, len(arr) - 1):
            if arr[i] == 1 and arr[i - 1] == 0:
                return i

