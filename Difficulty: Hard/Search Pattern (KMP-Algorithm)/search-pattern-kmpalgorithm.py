#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        list_a = []
        n=len(pat)
        for i in range(len(txt)):
            if txt[i:i+n] == pat:
                list_a += [i]
        return list_a