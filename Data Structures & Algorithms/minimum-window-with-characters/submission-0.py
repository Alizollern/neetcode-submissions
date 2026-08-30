class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
            
        # Подсчитываем количество каждого символа в строке t
        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1
            
        # Количество уникальных символов, которые должны совпасть
        required = len(dict_t)
        
        # Указатели окна и счетчики
        l, r = 0, 0
        formed = 0
        window_counts = {}
        
        # Храним минимальное окно: (длина, левая граница, правая граница)
        ans = float("inf"), None, None
        
        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Если текущий символ есть в t и его количество в окне совпадает с требуемым
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
                
            # Пробуем сузить окно слева, пока оно остается валидным
            while l <= r and formed == required:
                char = s[l]
                
                # Обновляем минимальное окно, если нашли вариант короче
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                    
                # Убираем левый символ из окна
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                    
                l += 1
                
            r += 1
            
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]