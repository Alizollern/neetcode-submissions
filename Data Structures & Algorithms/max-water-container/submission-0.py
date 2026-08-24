class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Вычисляем текущую площадь
            width = right - left
            current_height = min(height[left], height[right])
            current_water = width * current_height
            
            # Обновляем максимальный объем
            if current_water > max_water:
                max_water = current_water
                
            # Сдвигаем указатель с меньшей высотой
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water