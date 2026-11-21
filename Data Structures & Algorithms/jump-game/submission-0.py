class Solution:
    def canJump(self, nums: List[int]) -> bool:
        access=[False]*len(nums)
        if len(nums)==1:
            return True
        if not nums[0]:
            return False
        access[0]=True
        for i in range(len(nums)):
            if access[i] and nums[i]:
                for j in range (1,nums[i]+1):
                    if j+i<len(nums):
                        access[j+i]=True
        print(access)
        return access[-1]
