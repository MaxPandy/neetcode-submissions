class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(curr,length,seen):
            if length==len(nums):
                res.append(curr[:])
                return
            for i in nums:
                if i not in seen:
                    curr.append(i)
                    seen.add(i)
                    backtrack(curr,length+1,seen)
                    curr.pop()
                    seen.remove(i)
        backtrack([],0,set())
        return res