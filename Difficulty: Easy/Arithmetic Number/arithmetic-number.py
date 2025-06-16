#User function Template for python3

class Solution:
    def inSequence(self, a, b, c):
        # code here
        for i in range(a, b+1, c):
            if i == b:
                return 1
        return 0