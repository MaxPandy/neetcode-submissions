class Solution:
    def isHappy(self, n: int) -> bool:
        values=set()
        seen=False

        while n!=1 or seen:
            c=0
            while n:
                c+=(n%10)**2
                n//=10

            if c in values:
                return False
            values.add(c)
            n=c
        return True
