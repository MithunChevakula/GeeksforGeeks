#User function Template for python3

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        floorVal = -1         # initial val
        ceilIVal = -1
        floorDiff = float("inf")    # difference between target and arr[i]
        ceilDiff = float("inf")
        for i in range(len(arr)):
            fmin = x - arr[i]
            if fmin >=0 and fmin < floorDiff:
                floorVal = arr[i]
                floorDiff = fmin
            cmin = arr[i] - x 
            if cmin >=0 and cmin < ceilDiff:
                ceilIVal = arr[i]
                ceilDiff = cmin
                
        return floorVal, ceilIVal