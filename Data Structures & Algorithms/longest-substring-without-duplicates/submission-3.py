class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        obj = set()
        start, end, maxLen = 0, 0, 0
        for word in [*s]:
            while word in obj:
                obj.remove(s[start])
                start += 1
            end += 1
            maxLen = max(maxLen, end - start)
            obj.add(word)
        return maxLen