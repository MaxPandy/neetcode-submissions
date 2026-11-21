class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        val={}
        for num in bills:
            val[num]=1+val.get(num,0)
            if num==10:
                if val.get(5,0)==0:
                    return False
                val[5]-=1
            elif num==20:
                if val.get(5,0)<3 and (val.get(10,0)==0 or val.get(5,0)==0):
                    return False
                if val.get(10,0)>0:
                    val[5]-=1
                    val[10]-=1
                else:
                    val[5]-=3
        return True