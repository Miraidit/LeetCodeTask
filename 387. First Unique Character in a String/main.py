class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        for char in s:
            if char_freq[char] == 1:
                return s.index(char)
        return -1