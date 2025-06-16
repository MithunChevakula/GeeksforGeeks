class Solution:
    def inversionCount(self, arr):
        def merge_sort(arr):
            if len(arr) <= 1: return arr, 0
            mid = len(arr) // 2
            left, invL = merge_sort(arr[:mid])
            right, invR = merge_sort(arr[mid:])
            merged, i = [], 0
            inv = invL + invR
            j = k = 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    merged.append(left[j]); j += 1
                else:
                    merged.append(right[k]); inv += len(left) - j; k += 1
            merged += left[j:] + right[k:]
            return merged, inv
        return merge_sort(arr)[1]

