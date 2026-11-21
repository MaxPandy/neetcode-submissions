class Solution:
    def jump(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp[-1]=1
        for i in range(len(nums)-2,-1,-1):
            end=min(len(nums),i+1+nums[i])
            min_jump=float('inf')
            for j in range(i+1,end):
                if dp[j] and dp[j]+1<min_jump:
                    min_jump=dp[j]+1
            dp[i]=min_jump
        return dp[0]-1
