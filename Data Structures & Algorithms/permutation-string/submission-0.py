class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1_count = [0] * 26
        window_count = [0] * 26
        
        # 1. Заполняем эталон (s1) и самое первое окно в s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
            
        # Сразу проверяем первое окно
        if s1_count == window_count:
            return True
            
        # 2. Двигаем окно фиксированного размера до конца s2
        for i in range(len(s1), len(s2)):
            # Добавляем символ, который зашел в окно справа
            window_count[ord(s2[i]) - ord('a')] += 1
            
            # Убираем символ, который вышел из окна слева
            left_char = s2[i - len(s1)]
            window_count[ord(left_char) - ord('a')] -= 1
            
            # Проверяем, совпали ли массивы (сравнение 26 элементов работает за O(1))
            if s1_count == window_count:
                return True
                
        return False