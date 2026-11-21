class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums1=nums[:]
        nums2=nums[:]
        for i in range(1,len(nums)):
            nums1[i]=nums1[i]+nums1[i-1]
            nums2[len(nums)-i-1]=nums2[len(nums)-i-1]+nums2[len(nums)-i]
        count=0
        while count<len(nums):
            if nums1[count]==nums2[count]:
                return count
            count+=1
        return -1
