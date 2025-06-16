
from typing import List


class Solution:
    def findPair(self, arr: List[int], x: int) -> int:

        s=set()

        for i in arr:

            dif=i-x

            dif1=i+x

            if dif in s or dif1 in s:

                return(True)

            elif dif not in s and dif1 not in s:

                s.add(i)

            else:

                return(False)
        
