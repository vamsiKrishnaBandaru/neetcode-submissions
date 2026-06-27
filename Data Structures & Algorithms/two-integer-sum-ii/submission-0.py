class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        obj = {}
        for i in range(len(numbers)):
            if (target - numbers[i]) in obj:
                return [obj[target - numbers[i]], i + 1]
            obj[numbers[i]] = i + 1
        return []