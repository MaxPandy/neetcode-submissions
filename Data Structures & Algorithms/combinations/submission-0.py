class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        curr_comb=[]
        def backtrack(curr_comb,prev):
            if len(curr_comb)==k:
                res.append(curr_comb[:])
                return
            elif n-prev<k-len(curr_comb):
                return

            for i in range(prev+1,n+1):
                curr_comb.append(i)
                backtrack(curr_comb,i)
                curr_comb.pop()
        backtrack(curr_comb,0)
        return res