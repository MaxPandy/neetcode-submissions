class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1

        nums=[0]*(n+1)
        nums[1]=nums[2]=1
        for i in range (3,len(nums)):
            nums[i]=nums[i-1]+nums[i-2]+nums[i-3]
        return nums[-1]