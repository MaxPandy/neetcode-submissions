class Solution:
    def climbStairs(self, n: int) -> int:
        memory=[0]*(n+1)
        memory[0]=memory[1]=1
        return self.helper(n,memory)

    def helper(self,n:int, memory) ->int:
        if memory[n]:
            return memory[n]
        solution= self.helper(n-1,memory)+self.helper(n-2,memory)
        memory[n]=solution
        return solution