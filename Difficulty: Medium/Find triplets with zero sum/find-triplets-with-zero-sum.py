class Solution:
    # Function to find triplets with zero sum.
    def findTriplets(self, arr):
        #code here
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                complement = 0 - (arr[i]+arr[j])
                new_arr = arr[:i] + arr[i+1:j] + arr[j+1:]
                if complement in new_arr:
                    return True
        return False