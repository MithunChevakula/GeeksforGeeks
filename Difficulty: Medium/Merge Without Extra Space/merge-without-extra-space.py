class Solution:
    def mergeArrays(self, a, b):
        # code here
        res = [0] * (len(a) + len(b))
        i, j, k = 0, 0, 0

        # Merge the two arrays into res
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                res[k] = a[i]
                i += 1
            else:
                res[k] = b[j]
                j += 1
            k += 1

        # Add remaining elements from array a (if any)
        while i < len(a):
            res[k] = a[i]
            i += 1
            k += 1

        # Add remaining elements from array b (if any)
        while j < len(b):
            res[k] = b[j]
            j += 1
            k += 1

        # Copy the merged elements back to arrays a and b
        for i in range(len(a)):
            a[i] = res[i]
        for j in range(len(b)):
            b[j] = res[len(a) + j]