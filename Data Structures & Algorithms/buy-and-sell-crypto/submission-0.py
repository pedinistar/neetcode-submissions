class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointers left = l = buy & right = r = sell
        l, r = 0, 1
        maxP = 0 # to store max value at which i will sell

        # until the r is small than the length of prices
        while r < len(prices):
            # check if there is a profit
            if prices[l] < prices[r]:
                # calc the profit
                profit = prices[r] - prices[l]
                # now compare the profit with maxp
                maxP = max(maxP, profit)
            # if l is not small than r
            else:
                l = r
            # increase r with each iteration
            r += 1

        return maxP