class Solution:
    def reverseexponentiation(self, n):
        # code here
        rev=0
        a=n
        while(n!=0):
            rem=n%10
            rev=rev*10+rem
            n//=10
            
        p=pow(a,rev)
        return p