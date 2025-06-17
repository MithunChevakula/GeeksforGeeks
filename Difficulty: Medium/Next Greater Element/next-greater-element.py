class Solution:
    def nextLargerElement(self, arr):
        # code here
        stk = []
        ans = []
        for item in arr[::-1]:
            while stk and item >= stk[-1]: stk.pop()
            if not stk: ans.append(-1)
            else: ans.append(stk[-1])
            stk.append(item)
        return ans[::-1]