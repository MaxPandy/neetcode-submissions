class Solution:
    def isPalindrome(self, s: str) -> bool:
        check=''
        for i in s:
            if i.isalpha():
                check+=i.lower()
            elif i in '0123456789':
                check+=i
        print(check)
        if check==check[::-1]:
            return True
        return False