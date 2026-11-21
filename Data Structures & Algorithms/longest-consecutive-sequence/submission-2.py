class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        val={}
        for i in nums:
            val[i]=1
        max_length=0
        
        i=0
        for key in val:
            if key-1 not in val:
                j=1
                while key+j in val:
                    j+=1
                max_length=max(j,max_length)
        return max_length

