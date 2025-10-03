class Solution:
    def possibleWords(self, arr):
        # code here
        def f(ind, s):
            
            if ind >= n:
                res.append(s)
                return
            if arr[ind] in d:
                for i in d[arr[ind]]:
                    f(ind + 1, s + i)
            else:
                f(ind + 1, s)
                    
        d = {
            2: "abc",
            3: "def", 
            4: "ghi", 
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
            
        }
        n = len(arr)
        res = []
        f(0, '')
        return res
        