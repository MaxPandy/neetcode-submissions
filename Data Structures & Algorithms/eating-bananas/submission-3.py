import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        minimum=high
        while low<=high:
            mid=(low+high)//2
            hours=0
            for i in piles:
                hours+=math.ceil(i/mid)
            if h<hours:
                low=mid+1
            else:
                minimum=mid
                high=mid-1
        return minimum

