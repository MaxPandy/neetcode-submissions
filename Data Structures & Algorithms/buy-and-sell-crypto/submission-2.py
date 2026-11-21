class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy=prices[0]
        max_profit=0

        for sell in prices:
            max_profit=max(max_profit,sell-minBuy)
            minBuy=min(minBuy,sell)
        return max_profit