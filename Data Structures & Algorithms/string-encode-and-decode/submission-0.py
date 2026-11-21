class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for word in strs:
            for char in word:
                s+=chr((ord(char)+1)%256)
            s+='€'
        return s
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            word=''
            while s[i]!='€':
                word+=chr((ord(s[i])-1)%256)
                i+=1
            res.append(word)
            i+=1
        return res
