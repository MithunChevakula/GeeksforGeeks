#User function Template for python3

class Solution:
	def reverseDigits(self, n):
		# Code here
		rev=0
		while(n!=0):
		    rem=n%10
		    rev=rev*10+rem
		    n//=10
		return rev