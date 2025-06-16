#User function Template for python3

#Function to return the count of the number of elements in
#the intersection of two arrays.
class Solution:
    def numberofElementsInIntersection(self,a, b):
        #return: expected length of the intersection array.
        
        #code here
        return len(set(a).intersection(set(b)))