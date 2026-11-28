class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length=0
        max_string=''
        for c in range(len(s)):
            for l,r in ((c,c),(c,c+1)):
                while l>=0 and r<len(s) and s[l]==s[r]:
                    if max_length<r-l+1:
                        max_length=r-l+1
                        max_string=s[l:r+1]
                    l-=1
                    r+=1
        return max_string

                        
                        