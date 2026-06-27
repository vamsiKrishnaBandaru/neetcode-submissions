class Solution:
    def isValid(self, s: str) -> bool:
        obj = {')':'(', '}':'{', ']':'['}
        arr = []
        for i in s:
            if arr and i in obj and arr[-1] == obj[i]:
                arr.pop()
            else:
                arr.append(i)
        return not arr