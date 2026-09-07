class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Объединяем позицию и скорость, сортируем по убыванию позиции
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        current_slowest_time = 0.0
        
        for p, s in cars:
            # Вычисляем время для текущей машины
            time_to_target = (target - p) / s
            
            # Если время больше, чем у флота впереди, она образует новый флот
            if time_to_target > current_slowest_time:
                fleets += 1
                current_slowest_time = time_to_target
                
        return fleets