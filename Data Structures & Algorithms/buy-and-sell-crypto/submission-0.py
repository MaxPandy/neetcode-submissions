class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j=0,0
        cur_val=0
        max_val=0
        while i<len(prices)-1:
            i+=1
            curr_val=prices[i]-prices[j]
            max_val=max(max_val,curr_val)
            if curr_val<=0:
                j=i
        return max_val