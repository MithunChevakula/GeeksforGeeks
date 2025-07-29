class Solution:
    def findTriplet(self, arr):
        for i in range(len(arr)):

            for j in range(i+1,len(arr)):

                s = arr[i]+arr[j]

                if s in arr:

                    return True

        return False
                