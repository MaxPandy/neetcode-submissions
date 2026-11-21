class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""     
        val={}
        for char in t:
            val[char]=1+val.get(char,0)
    
        val2={}
        i=0
        best_len=float('inf')
        best_i=0

        have=0
        need=len(val)

        for j in range(len(s)):
            val2[s[j]]=1+val2.get(s[j],0)
            if s[j] in val and val[s[j]]==val2[s[j]]:
                have+=1
            
            while have==need:
                if j-i+1<best_len:
                    best_len=j-i+1
                    best_i=i

                if s[i] in val and val[s[i]]==val2[s[i]]:
                    have-=1
                val2[s[i]]-=1
                i+=1
        return "" if best_len==float('inf') else s[best_i:best_i+best_len]
    

        