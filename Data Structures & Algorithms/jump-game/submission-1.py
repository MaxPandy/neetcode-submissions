class Solution:
    def canJump(self, nums: List[int]) -> bool:
        access=[False]*len(nums)
        access[-1]=True

        for i in range(len(nums)-2,-1,-1):
            end=min(len(nums),i+1+nums[i])
            for j in range(i+1,end):
                if access[j]:
                    access[i]=True
                    break
        return access[0]

