class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        
        dyn=[-1]*(amount+1)
        for i in coins:
            if i<=amount:
                dyn[i]=1

        for i in range(len(dyn)):
            if dyn[i]==-1:
                minimum=float('inf')
                for coin in coins:
                    if i-coin>0 and dyn[i-coin]!=-1:
                        minimum=min(minimum,dyn[i-coin])
                if minimum!=float('inf'):
                    dyn[i]=minimum+1
        print(dyn)
        return dyn[-1]


