class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # Если символ уже есть в окне, сдвигаем левую границу
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1
            # Добавляем текущий символ в окно
            seen_chars.add(s[right])
            # Обновляем максимальную длину
            max_len = max(max_len, right - left + 1)
        
        return max_len