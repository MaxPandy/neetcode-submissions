class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_index=-1
        k=0
        for i in range (len(nums)):
            if val_index==-1 and nums[i]==val:
                val_index=i
            else:
                if nums[i]!=val:
                    k+=1
                    if val_index!=-1:
                        nums[i],nums[val_index]=nums[val_index],nums[i]
                        val_index+=1
        return(k)