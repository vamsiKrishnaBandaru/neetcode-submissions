class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        for i in range(1, len(height) - 1):
            leftMax = max(height[:i])
            rightMax = max(height[i + 1:])
            water = min(leftMax, rightMax) - height[i]
            if water > 0:
                count += water
        return count