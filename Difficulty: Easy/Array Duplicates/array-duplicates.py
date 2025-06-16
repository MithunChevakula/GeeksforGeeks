class Solution:
    def findDuplicates(self, arr):
        # code here
        d = {}
        ls = []
        for num in arr:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        for k,v in d.items():
            if v >1:
                ls.append(k)
        return ls
        