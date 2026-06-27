class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        obj = {}
        for i in nums:
            obj[i] = obj.get(i, 0) + 1
        
        for _ in range(k):
            maxKey = 0
            maxTimes = -1
            for key in obj:
                if obj[key] > maxTimes:
                    maxKey = key
                    maxTimes = obj[key]
            result.append(maxKey)
            obj[maxKey] = 0
        return result[:k]