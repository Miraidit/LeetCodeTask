class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_split = s.split()
        n = str_split[::-1]
        return(len(n[0]))