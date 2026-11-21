class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)

        for i,temp in enumerate(temperatures):
            if not stack:
                stack.append((i,temp))
            else:
                while stack and stack[-1][1]<temp:
                    el=stack.pop()
                    res[el[0]]=i-el[0]
                stack.append((i,temp))
        return res


