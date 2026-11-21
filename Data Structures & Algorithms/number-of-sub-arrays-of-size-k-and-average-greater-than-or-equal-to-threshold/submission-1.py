class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        avg=sum(nums[:k])
        counter=0
        for i in range(len(nums)-k):
            if avg>=threshold*k:
                counter+=1
            avg=avg-nums[i]+nums[k+i]
        if avg>=threshold*k:
            counter+=1
        return counter