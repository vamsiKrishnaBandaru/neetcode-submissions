class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1] * n
        prefix = 1
        for i in range(n):
            arr[i] = prefix
            prefix *= nums[i]
        sufix = 1
        for i in range(n - 1, -1, -1):
            arr[i] *= sufix
            sufix *= nums[i]
        return arr