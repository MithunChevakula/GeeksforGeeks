#User function Template for python3
class Solution:
    def maximumSumSubarray (self,arr,k):
        # code here
        current_sum=sum(arr[:k])
        res=current_sum
        for i in range(len(arr)-k):
            current_sum=current_sum-arr[i]+arr[i+k]
            res=max(current_sum,res)
        return res