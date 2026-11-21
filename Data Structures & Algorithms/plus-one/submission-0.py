class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=0
        for i in range(len(digits)):
            number+=digits[i]*10**(len(digits)-1-i)
        number+=1
        return list(map(int,str(number)))