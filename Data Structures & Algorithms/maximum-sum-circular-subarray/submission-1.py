class Solution:
    def KadaneMax(self,nums):
        maxSum=nums[0]
        currSum=0

        for n in nums:
            currSum=max(currSum,0)
            currSum+=n
            maxSum=max(maxSum,currSum)
        return maxSum

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=sum(nums)
        maxK=self.KadaneMax(nums)
        minimum=-self.KadaneMax([-n for n in nums])
        minK=total-minimum
        if maxK<0:
            return maxK
        return max(maxK,minK)