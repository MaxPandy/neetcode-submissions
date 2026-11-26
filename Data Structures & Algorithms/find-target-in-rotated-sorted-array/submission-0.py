class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_start(nums):
            lo,hi=0,len(nums)-1
            while lo<hi:
                mid=(lo+hi)//2
                if nums[mid]>nums[hi]:
                    lo=mid+1
                else:
                    hi=mid
            return lo
            
        def find_target(nums,target):
            start=find_start(nums)

            lo,hi=start-len(nums),start-1
            while lo<=hi:
                mid=(lo+hi)//2
                if nums[mid]==target:
                    return mid%len(nums)
                if nums[mid]>target:
                    hi=mid-1
                else:
                    lo=mid+1
            return -1

        return find_target(nums,target)

