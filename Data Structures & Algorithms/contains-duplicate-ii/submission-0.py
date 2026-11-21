class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        values={}
        for i,value in enumerate(nums):
            print(i,value)
            if value in values and i-values[value]<=k:
                return True
            values[value]=i
        return False