class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets=[0]*3
        for i in nums:
            buckets[i]+=1
        i=0
        for color in range(3):
            for j in range(buckets[color]):
                nums[i]=color
                i+=1

        
        