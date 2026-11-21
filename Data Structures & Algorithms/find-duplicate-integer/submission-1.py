class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        val={}
        for i in range(len(nums)):
            if nums[i] in val.keys():
                return nums[i]
            val[nums[i]]=1
            