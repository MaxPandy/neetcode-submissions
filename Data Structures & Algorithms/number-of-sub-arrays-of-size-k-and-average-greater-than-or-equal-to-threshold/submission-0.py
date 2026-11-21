class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        avg=sum(nums[:k])/k
        counter=0
        for i in range(len(nums)-k):
            print(nums[k+i])
            if avg>=threshold:
                counter+=1
            avg=(k*avg-nums[i]+nums[k+i])/k
        if avg>=threshold:
            counter+=1
        return counter