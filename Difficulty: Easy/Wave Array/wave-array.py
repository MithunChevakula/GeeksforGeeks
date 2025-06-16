from typing import List


class Solution:
    def convertToWave(self, arr : List[int]) -> None:
        # code here
        for i in range(0,len(arr),2) :
            if i != len(arr)-1:
                arr[i], arr[i+1] = arr[i+1], arr[i]
