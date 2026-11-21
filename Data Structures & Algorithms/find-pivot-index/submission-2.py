class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        leftSum=0
        for i in range(len(nums)):
            leftSum+=nums[i]
            rightSum=total-leftSum+nums[i]
            if rightSum==leftSum:
                return i
        return -1