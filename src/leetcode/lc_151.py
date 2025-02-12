class Solution:
    def reverseWords(self, s: str) -> str:
        clean_s = s.strip()
        result = clean_s.split()

        return " ".join(result[::-1])
