class Solution:
    def rearrange(self, arr, x):
        # code here
        arr.sort(key=lambda a: abs(x-a))
        