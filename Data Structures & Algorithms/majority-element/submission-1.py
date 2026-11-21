class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val={}
        for num in nums:
            val[num]=1+val.get(num,0)
        return max(val, key=val.get)