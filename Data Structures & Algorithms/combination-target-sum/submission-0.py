class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        curr_sum=[]
        def backtrack(start,curr_sum, target_val):
            if not target_val:
                if curr_sum not in res:
                    res.append(curr_sum[:])
            if start==len(nums) or target_val<0:
                return

            val=nums[start]
            curr_sum.append(val)
            backtrack(start,curr_sum,target_val-val)
            curr_sum.pop()
            backtrack(start+1,curr_sum,target_val)

        backtrack(0,[],target)
        return res