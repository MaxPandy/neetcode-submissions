class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for c in range(len(s)):
            for l,r in ((c,c),(c,c+1)):
                while l>=0 and r<len(s) and s[l]==s[r]:
                    count+=1
                    l-=1
                    r+=1
        return count        