class Solution:
    def trap(self, height: List[int]) -> int:
        prefix=[0]*len(height)
        suffix=[0]*len(height)
        n=len(height)
        prefix_max,suffix_max=0,0
        for i in range(n):
            prefix_max=max(prefix_max,height[i])
            prefix[i]=prefix_max
            suffix_max=max(suffix_max,height[n-1-i])
            suffix[n-1-i]=suffix_max
        total=0
        for i in range(n):
            total+=min(prefix[i],suffix[i])-height[i]
        return total