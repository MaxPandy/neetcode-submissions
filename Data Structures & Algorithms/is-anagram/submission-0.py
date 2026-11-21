class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        set_s={}
        set_t ={}
        for i,letter in enumerate(s):
            if letter not in set_s:
                set_s[letter]=1
            else:
                set_s[letter]+=1
        
        for i,letter in enumerate(t):
            if letter not in set_t:
                set_t[letter]=1
            else:
                set_t[letter]+=1
        return set_t==set_s
       