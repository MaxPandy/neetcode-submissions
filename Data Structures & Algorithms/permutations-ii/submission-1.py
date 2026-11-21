class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=[False]*len(nums)
        nums.sort()
        def backtrack(curr,length):
            if length==len(nums):
                res.append(curr[:])
                return
            for i in range (len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                curr.append(nums[i])
                used[i]=True
                backtrack(curr,length+1)
                curr.pop()
                used[i]=False

        backtrack([],0)
        return res