#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
		# Complete this function
		n = len(mat)
		m = len(mat[0])
		for i in range(n):
		    for j in range(m):
		        if mat[i][j] == x:
		            return True
		return False