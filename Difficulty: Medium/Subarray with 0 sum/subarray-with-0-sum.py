#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr):
        ##Your code here
        #Return true or false
        prefix_sum_set = set()
        prefix_sum = 0
        for num in arr:
            prefix_sum += num
            if prefix_sum == 0 or prefix_sum in prefix_sum_set:
                return True
            prefix_sum_set.add(prefix_sum)
        return False