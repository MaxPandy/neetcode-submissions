class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r,counter,unique=0,1,0,1
        while r<len(nums):
            if nums[r]==nums[l] and not counter:
                l+=1
                nums[l]=nums[r]
                counter+=1
                unique+=1
            elif nums[r]!=nums[l]:
                l+=1
                nums[l]=nums[r]
                counter=0
                unique+=1
            r+=1
            print(nums, unique)
        return unique