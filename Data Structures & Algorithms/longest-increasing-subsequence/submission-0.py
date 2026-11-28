class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res=[1]*len(nums)
        for i in range(len(nums)):
            max_size=1
            for j in range(0,i):
                if nums[j]<nums[i]:
                    max_size=max(max_size,res[j]+1)
            res[i]=max_size
        print(res)
        return max(res)
            