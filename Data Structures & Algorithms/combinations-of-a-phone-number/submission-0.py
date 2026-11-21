class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        res=[]
        char={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs",
              "8":"tuv","9":"wxyz"}
        def backtracking(array,length):
            if length==len(digits):
                res.append(array[:])
                return
            for letter in char[digits[length]]:
                backtracking(array+letter,length+1)
        backtracking("",0)
        return res