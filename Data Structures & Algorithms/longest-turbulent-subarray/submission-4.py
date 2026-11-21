class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 1
        L=0
        case=-1
        max_length=1

            
        for R in range(len(arr)-1):
            if arr[R]==arr[R+1]:
                L=R+1
                case=-1
            elif case==-1:
                case=1 if arr[R]>arr[R+1] else 0
            elif (arr[R]>arr[R+1] and case==0) or (arr[R]<arr[R+1] and case==1):
                case=1 if arr[R]>arr[R+1] else 0
            else:
                L=R
                case=1 if arr[R]>arr[R+1] else 0
                
            max_length=max(max_length,R-L+2)
        return max_length
        