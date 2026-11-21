class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=k-1
        val={}
        max_size=0
        max_arr=0
        sum_arr=0

        for letter in range(0,k):
            val[s[letter]]=1+val.get(s[letter],0)
            sum_arr+=1
            max_arr=max(max_arr,val[s[letter]])
        
        while j<len(s)-1:
            free=k-(sum_arr-max_arr)
            if free>=0:
                max_size=max(max_size,j-i+1)
                j+=1
                val[s[j]]=1+val.get(s[j],0)
                sum_arr+=1
                max_arr=max(max_arr,val[s[j]])
            else:
                sum_arr-=1
                val[s[i]]-=1
                i+=1
        if k - (sum_arr - max_arr) >= 0:
            max_size = max(max_size, j - i + 1)   
        return max_size