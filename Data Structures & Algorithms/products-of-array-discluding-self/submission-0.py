class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        output=[1]*len(nums)
        zeros=0
        for num in nums:
            if num!=0:
                product*=num
            else:
                zeros+=1
        for i in range(len(nums)):
            if zeros==1:
                output[i]=0 if nums[i]!=0 else product
            elif zeros>1:
                output[i]=0
            else:
                output[i]=product//nums[i]
        return output