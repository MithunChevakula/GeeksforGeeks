#User function Template for python3

class Solution:
    def allPairs(self, target, arr1, arr2):
        # Your code goes here
        l={}

        m=[]

        for j in arr2:

            if j not in l:

                l[j]=1

            else:

                l[j]+=1

        for i in range(len(arr1)):

            res=target-arr1[i]

            if res in l:

                for _ in range(l[res]):

                    m.append((arr1[i],res))

        return sorted(m)
    
