class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        vals={0:1}
        total=0
        for x in nums:
            prefix+=x
            total+=vals.get(prefix-k,0)
            vals[prefix]=1+vals.get(prefix,0)
        return total
