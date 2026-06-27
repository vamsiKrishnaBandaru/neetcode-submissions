class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        obj = {}
        for word in strs:
            temp = "".join(sorted(word))
            if temp in obj:
                obj[temp].append(word)
            else:
                obj[temp] = [word]
        return list(obj.values())