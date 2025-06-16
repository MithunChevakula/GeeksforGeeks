# User function Template for python3

class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        #code here
        arr1, arr2 = a, b
        hash_map = {}
        m, n = len(arr1), len(arr2)
        # Array length should be same for equality
        if m != n:
            return False

        for i in range(n):
            # Storing the count of element of both the arrays using dict getter with default value 0
            hash_map[arr1[i]] = hash_map.get(arr1[i], 0) + 1
            hash_map[arr2[i]] = hash_map.get(arr2[i], 0) - 1
            # Deletion of key once it is present in both array and get balanced to 0
            if arr1[i] in hash_map and hash_map[arr1[i]] == 0:
                del hash_map[arr1[i]]
            if arr2[i] in hash_map and hash_map[arr2[i]] == 0:
                del hash_map[arr2[i]]
        
        # In case of unequal arrays hash_map will contain keys with some negative or positive integer value 
        return True if len(hash_map.keys()) == 0 else False