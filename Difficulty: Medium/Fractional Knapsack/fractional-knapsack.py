class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        #code here
        items=[]
        for i in range(len(wt)):
            items.append((val[i],wt[i]))
        items.sort(key=lambda x:x[0]/x[1],reverse=True)
        totalvalue=0.0
        for value,weight in items:
            if capacity>=weight:
                capacity-=weight
                totalvalue+=value
            else:
                frac=capacity/weight
                totalvalue+=frac*value
                break
        return totalvalue