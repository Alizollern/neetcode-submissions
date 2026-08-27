class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # Если символ уже встречался И его индекс находится внутри нашего текущего окна
            if current_char in char_index_map and char_index_map[current_char] >= left:
                # Сдвигаем левую границу окна за предыдущее вхождение этого символа
                left = char_index_map[current_char] + 1
            
            # Обновляем индекс текущего символа
            char_index_map[current_char] = right
            
            # Считаем длину текущего окна и обновляем максимум
            max_length = max(max_length, right - left + 1)
            
        return max_length