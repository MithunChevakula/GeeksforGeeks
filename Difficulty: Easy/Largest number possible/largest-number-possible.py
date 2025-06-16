class Solution:
    def findLargest(self, N, S):
        # code here
        if S == 0 and N > 1 or S > 9 * N:
            return -1
        res = []
        for i in range(N):
            digit = min(9,S)
            res.append(str(digit))
            S = S-digit
        ans = ''.join(res)
        return ans