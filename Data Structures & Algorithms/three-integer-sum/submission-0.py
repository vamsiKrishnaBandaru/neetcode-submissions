class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                target = nums[l] + nums[r] + nums[i]
                if target == 0:
                    result.append([nums[l], nums[r], nums[i]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1  
                elif target < 0:
                    l += 1
                else:
                    r -= 1
        return result