#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def mergeSort(self, arr, l, r):
        if l < r:
            mid = (l + r) // 2  # Find the middle point
            
            # Recursively sort the left and right halves
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            
            # Merge the sorted halves
            self.merge(arr, l, mid, r)

    def merge(self, arr, l, mid, r):
        left_part = arr[l:mid+1]
        right_part = arr[mid+1:r+1]

        i = j = 0  # Pointers for left and right subarrays
        k = l  # Pointer for merging in original array

        # Merge elements in sorted order
        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1
        
        # Copy any remaining elements from left_part
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1

        # Copy any remaining elements from right_part
        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1



#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.mergeSort(arr,0,len(arr)-1)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends