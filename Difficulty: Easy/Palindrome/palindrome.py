class Solution:
    def isPalindrome(self, n):
        num = n
        rev = 0
        while n>0:
            dig = n%10
            rev = rev *10 +dig
            n//=10
        return (rev==num)