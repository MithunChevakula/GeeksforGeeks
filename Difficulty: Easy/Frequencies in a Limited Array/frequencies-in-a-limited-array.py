class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        #  code here
        dict={}
        n=len(arr)
        for i in arr:
            dict[i]=dict.get(i,0)+1
        res=[]
        for i in range(1,n+1):
            res.append(dict.get(i,0))
        return res

