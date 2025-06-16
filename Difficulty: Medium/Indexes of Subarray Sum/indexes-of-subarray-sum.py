#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        start = 1
        end = 1
        val = arr[0]
        while start<len(arr)+1:
            # temp = arr[start-1:end]
            # print(start,end,val)
            # val = sum(temp)
            if val == target:
                return [start,end]
            elif val < target and end < len(arr):
                val += arr[end]
                end += 1
            else:
                val -= arr[start-1]
                start += 1
        return [-1]

