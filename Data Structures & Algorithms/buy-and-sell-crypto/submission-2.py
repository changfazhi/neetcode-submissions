class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n time and constant space
        # should have 2 pointers, if the profit is bad, move r pointer, 
        n = len(prices)
        left = 0
        right = 1
        maxP = 0
        for i in range(n-1):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right
            right += 1
        
        return maxP
        