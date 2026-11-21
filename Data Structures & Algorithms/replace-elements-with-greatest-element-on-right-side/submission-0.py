class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_arr=[]
        for i in range (len(arr)-1):
            max_arr.append(max(arr[i+1:]))
        max_arr.append(-1)
        return max_arr