
from typing import List


class Solution:
    def zigZag(self,arr : List[int]) -> None:
        # code here
        flag = True
        for i in range(len(arr)):    
            arr[i] = 1 if flag else 2
            flag = not flag
        
