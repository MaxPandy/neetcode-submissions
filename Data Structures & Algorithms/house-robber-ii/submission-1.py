class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def rob1(nums):
            res=[0]*(len(nums)+2)
            for i in range(2,len(res)):
                res[i]=max(res[i-1],res[i-2]+nums[i-2])
            return res[-1]
        return max(rob1(nums[1:]),rob1(nums[:-1]))
            