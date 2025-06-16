#User function template for Python

class Solution:
    def removeDuplicates(self, arr):
        #Code Here
        if not arr:
            return 0

        unique_index = 0
        for i in range(1, len(arr)):
            if arr[i] != arr[unique_index]:
                unique_index += 1
                arr[unique_index] = arr[i]
        return unique_index + 1