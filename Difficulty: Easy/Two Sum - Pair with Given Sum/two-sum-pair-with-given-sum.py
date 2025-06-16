class Solution:
	def twoSum(self, arr, target):
		# code here
		arr = sorted(arr)
        left, right = 0, len(arr)-1
        while left<right:
            x = arr[left]+arr[right]
            if target==x:
                return True
            elif target>x:
                left+=1
            else:
                right -=1
        return False