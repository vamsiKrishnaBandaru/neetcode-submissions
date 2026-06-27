class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''
        for i in [*s]:
            if i.isnumeric() or i.isalpha():
                a+=i.lower()
        return a==a[::-1]