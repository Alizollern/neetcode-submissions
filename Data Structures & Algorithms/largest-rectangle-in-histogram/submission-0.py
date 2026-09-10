class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # stores indices of bars
        max_area = 0
        n = len(heights)
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # If stack is empty, width spans from 0 to i
                # Otherwise, width spans from the previous stack index + 1 to i - 1
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
            
        # Process remaining bars in the stack
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)
            
        return max_area