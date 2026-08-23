class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Шаг 1: Сортировка массива
        nums.sort()
        res = []
        
        # Шаг 2: Фиксация первого числа
        for i in range(len(nums)):
            # Оптимизация: если число больше нуля, сумма уже не даст 0
            if nums[i] > 0:
                break
                
            # Пропуск дубликатов для первого числа
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Шаг 3: Метод двух указателей
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    # Сумма слишком маленькая, двигаем левый указатель вправо
                    left += 1
                elif total > 0:
                    # Сумма слишком большая, двигаем правый указатель влево
                    right -= 1
                else:
                    # Нашли тройку!
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Шаг 4: Пропуск дубликатов для оставшихся чисел
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return res