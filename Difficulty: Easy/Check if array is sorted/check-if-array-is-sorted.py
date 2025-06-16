class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        # code here
        for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                return False
            
        return True