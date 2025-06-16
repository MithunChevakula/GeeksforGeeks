class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        n = len(arr)
        if x in arr:
            c = arr.count(x)
            return arr.index(x)+c-1
        else:
            if n == 1 and arr[0] < x:
                return 0
            if arr[n-1] < x:
                return n-1
            for i in range(n):
                if arr[i] > x:
                    return i-1
        return -1
        