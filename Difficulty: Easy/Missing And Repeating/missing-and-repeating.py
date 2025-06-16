#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n=len(arr)
        a=list(set(arr))
        
        sum1=sum(a) 
        actual_sum=sum(arr) 
        duplicate_ele = actual_sum-sum1 
        expected_sum=n*(n+1)//2 
        missing_ele = expected_sum-(actual_sum-duplicate_ele) 
        lists=[duplicate_ele,missing_ele]
        return lists

