class Solution:

	def findLargest(self, arr):
	    # code here
	    from functools import cmp_to_key
        arr_str = list(map(str, arr))
        
        def compare(a, b):
            if a + b < b + a:
                return 1
            else:
                return -1
        
        arr_str.sort(key=cmp_to_key(compare))
        if arr_str[0] == "0":
            return "0"
        return "".join(arr_str)
	    