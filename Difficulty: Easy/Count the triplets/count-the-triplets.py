class Solution:
	def countTriplet(self, arr):
		# code here
		count = 0
        arr.sort()
        n = len(arr)
        
        for i in range(n - 1, 1, -1):
            c = arr[i]
            left = 0
            right = i - 1
            while left < right:
                if arr[left] + arr[right] == c:
                    count += 1
                    left += 1
                    right -= 1
                elif arr[left] + arr[right] < c:
                    left += 1
                else:
                    right -= 1
        return count

