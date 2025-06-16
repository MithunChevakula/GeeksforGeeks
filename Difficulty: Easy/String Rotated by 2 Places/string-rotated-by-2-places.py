#User function Template for python3


class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,s1,s2):
        #code here
        return s1[2:] + s1[:2] == s2 or s2[2:] + s2[:2] == s1