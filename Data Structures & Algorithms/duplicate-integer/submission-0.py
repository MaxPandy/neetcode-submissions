class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elem={}
        for i in nums:
            if not elem.get(i):
                elem[i]=1
            else:
                return True
        return False