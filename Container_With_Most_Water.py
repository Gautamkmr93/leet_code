from typing import List

class Calculate_Area:
    def Calculate_maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i, h1 in enumerate(height):
            for w, h2 in enumerate(height[i + 1:], 1):
                h = min(h1, h2)
                area = w * h
                if area > max_area:
                    max_area = area
        return max_area

given_list=[1,8,6,2,5,4,8,3,7]
a=Calculate_Area()
print(a.Calculate_maxArea([1,8,6,2,5,4,8,3,7]))