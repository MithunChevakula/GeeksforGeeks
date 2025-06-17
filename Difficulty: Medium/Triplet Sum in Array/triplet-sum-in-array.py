#User function Template for python3
class Solution:
    # Function to find if there exists a triplet in the array arr[] which sums up to target.
    def hasTripletSum(self, arr, target):
        # Your Code Here
        seen1=set()
        seen2=set()
        for ve in arr:
            if target-ve in seen2:
                return True
            for ve1 in seen1:
                seen2.add(ve1+ve)
            seen1.add(ve)
        return False