class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        for i in range(len(height) - 1):
            leftMax = max(height[:i]) if i > 0 else 0
            righMax = max(height[i:])
            minMax = min(leftMax, righMax)
            if minMax > height[i]:
                count += minMax - height[i]
        return count