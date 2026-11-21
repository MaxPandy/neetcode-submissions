class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=[False]*len(nums)
        nums.sort()
        def backtrack(curr,length):
            if length==len(nums):
                res.append(curr[:])
                return
            seen=set()
            for i,num in enumerate(nums):
                if used[i] or num in seen:
                    continue
                curr.append(num)
                used[i]=True
                backtrack(curr,length+1)
                curr.pop()
                used[i]=False
                seen.add(num)

        backtrack([],0)
        return res