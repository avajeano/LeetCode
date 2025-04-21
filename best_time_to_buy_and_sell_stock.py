# time: O(n) | space: O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # the day we buy
        left = 0
        # the day we sell
        right = 1

        maxProfit = 0

        while right < len(prices):
            # if the transaction is profitable 
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
            # lower number to buy 
            else:
                left = right
            right += 1
        return maxProfit
