class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) for time and space
        n = len(prices)
        hold, sold, rest = -prices[0], 0, 0

        for i in range(1, n):
            prev_sold = sold
            sold = hold + prices[i]
            hold = max(hold, rest - prices[i])
            rest = max(rest, prev_sold)
        
        return max(sold, rest)
        