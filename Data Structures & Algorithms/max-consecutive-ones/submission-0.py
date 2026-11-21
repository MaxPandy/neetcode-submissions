class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter=0
        max_number=0
        for i in range (len(nums)):
            if nums[i]:
                counter+=1
            else:
                max_number=max(max_number,counter)
                counter=0
        return max(max_number,counter)
        