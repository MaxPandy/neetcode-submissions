class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result=[]
        for i in operations:
            if i not in "+DC":
                result.append(int(i))
            elif i=="+":
                result.append(result[-1]+result[-2])
            elif i=="D":
                result.append(result[-1]*2)
            elif i=="C":
                result.pop()
        return sum(result)