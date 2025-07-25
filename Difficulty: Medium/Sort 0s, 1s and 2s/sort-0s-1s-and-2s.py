class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        low = 0
        mid = 0
        high = len(arr)-1
        
        while mid <= high:
            
            if arr[mid] == 0:
                arr[mid],arr[low] = arr[low],arr[mid]
                mid+=1
                low+=1
            elif arr[mid] == 2:
                arr[mid],arr[high] = arr[high],arr[mid]
                high-=1
            elif arr[mid] == 1:
                mid+=1
    
        return arr
        