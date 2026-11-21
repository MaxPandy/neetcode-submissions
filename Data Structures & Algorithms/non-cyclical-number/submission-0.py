class Solution:
    def isHappy(self, n: int) -> bool:
        values={}
        seen=False

        while n!=1 or seen:
            c=0
            while n:
                c+=(n%10)**2
                n//=10

            if c in values.keys():
                return False
            else:
                values[c]=True
            n=c
        return True
