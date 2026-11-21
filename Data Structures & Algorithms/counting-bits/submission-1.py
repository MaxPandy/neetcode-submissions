class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]
        if n==1:
            return [0,1]
        i=2
        res=[0,1]
        while i*2<=n:
            res.extend([x + y for x, y in zip(res, [1]*len(res))])
            i*=2

        for j in range(i,n+1):
            res.append(1+res[j-i])
        return res