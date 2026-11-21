class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue

            val=-nums[i]
            j,k=i+1,len(nums)-1

            while j<k:

                curr=nums[j]+nums[k]

                if curr<val:
                    j+=1
                elif curr>val:
                    k-=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j+1]==nums[j]:
                        j+=1
                    while j<k and nums[k-1]==nums[k]:
                        k-=1
                    j+=1
                    k-=1

        return res