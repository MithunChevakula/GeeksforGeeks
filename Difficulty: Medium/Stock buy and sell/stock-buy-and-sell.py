class Solution:
    #Function to find the days of buying and selling stock for max profit.
    def stockBuySell(self, arr):
        # code here
        n = len(arr) - 1 
        profit = 0
        for i in range(n):
            if arr[i] < arr[i + 1]:
                summ = arr[i+1] - arr[i]
                profit += summ
                
        return profit