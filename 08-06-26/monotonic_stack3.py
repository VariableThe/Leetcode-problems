class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start_index = i

            while stack and stack[-1][1] > h:
                popped_index, popped_height = stack.pop()

                area = popped_height * (i - popped_index)
                if area > max_area:
                    max_area = area

                start_index = popped_index

            stack.append((start_index, h))

        for index, height in stack:
            area = height * (len(heights) - index)
            if area > max_area:
                max_area = area

        return max_area
