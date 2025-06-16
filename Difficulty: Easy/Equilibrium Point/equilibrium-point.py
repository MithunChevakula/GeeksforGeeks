# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        left_sum = arr[0]
        right_sum = sum(arr)
        for i in range(1, len(arr)):
            left_sum += arr[i - 1]
            right_sum -= arr[i]
            if left_sum == right_sum:
                return i
        return -1

