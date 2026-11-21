class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        f1=1
        f2=2
        while n-2:
            temp=f2
            f2=f1+f2
            f1=temp
            n-=1
        return f2