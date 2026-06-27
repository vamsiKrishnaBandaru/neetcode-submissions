class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxLen = 0
        for i in seen:
            if (i - 1) in seen:
                continue
            temp = i + 1
            cont = 1
            while temp in seen:
                cont += 1
                temp += 1
            maxLen = max(maxLen, cont)
        return maxLen