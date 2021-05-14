class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def max_area(heights):
            stack = []
            maxArea = 0
            heights.append(0)
            N = len(heights)
            for i in range(N):
                if not stack or heights[i] > heights[stack[-1]]:
                    stack.append(i)
                else:
                    while stack and heights[i] <= heights[stack[-1]]:
                        h = heights[stack[-1]]
                        stack.pop()
                        if not stack:
                            w = i
                        else:
                            w = i - stack[-1] - 1
                        maxArea = max(maxArea, h * w)
                    stack.append(i)
            return maxArea

        
        maxArea = 0
        if not matrix: 
            return maxArea
        hist = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    hist[j] = hist[j] + 1
                else:
                    hist[j] = 0
            maxArea = max(maxArea, max_area(hist))
        return maxArea
