class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:
        values={}
        L=0
        length=0
        for R in range(len(nums)):
            if nums[R] in values and values[nums[R]]>=L:
                L=values[nums[R]]+1
            values[nums[R]]=R
            length=max(length,R-L+1)
        return length
                
            