class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
            
        val={}
        for char in s1:
            val[char]=1+val.get(char,0)
        length=len(s1)
        i,j=0,0
        
        val2={}
        while j<length:
            val2[s2[j]]=1+val2.get(s2[j],0)
            j+=1
            
        while j<len(s2):

            if val==val2:
                return True

            if val2[s2[i]]==1:
                val2.pop(s2[i])
            else:
                val2[s2[i]]-=1

            i+=1
            val2[s2[j]]=1+val2.get(s2[j],0)
            j+=1
        return val==val2

