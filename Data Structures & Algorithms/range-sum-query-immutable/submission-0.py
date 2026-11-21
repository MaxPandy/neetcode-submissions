class NumArray:

    def __init__(self, nums: List[int]):
       self.array=nums 
       for i in range (1,len(self.array)):
            self.array[i]=self.array[i]+self.array[i-1]

    def sumRange(self, left: int, right: int) -> int:
        if not left:
            return self.array[right]
        return self.array[right]-self.array[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)