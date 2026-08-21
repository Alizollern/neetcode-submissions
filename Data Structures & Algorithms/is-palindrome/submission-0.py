class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Пропускаем не буквенно-цифровые символы слева
            while left < right and not s[left].isalnum():
                left += 1
                
            # Пропускаем не буквенно-цифровые символы справа
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Сравниваем символы, приведя их к нижнему регистру
            if s[left].lower() != s[right].lower():
                return False
                
            # Сдвигаем указатели дальше
            left += 1
            right -= 1
            
        return True