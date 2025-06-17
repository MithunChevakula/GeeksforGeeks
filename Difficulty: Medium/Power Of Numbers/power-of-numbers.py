class Solution:
    def reverse_exponentiation(self, n):
        # code here
        a=str(n)
        a=int(a[::-1])
        return n**a