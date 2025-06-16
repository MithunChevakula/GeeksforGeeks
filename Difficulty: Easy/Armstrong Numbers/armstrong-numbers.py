#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here
        count=0
        n2=n
        sum=0
        temp=n
        while n>0: 
            n=n//10
            count+=1
        while n2>0:
            rem=n2%10
            sum+=rem**count 
            n2=n2//10
        
        if sum==temp:
            return True
        else:
            return False