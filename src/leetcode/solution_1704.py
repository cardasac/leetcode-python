

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels: set[str] = set("aeiouAEIOU")
        count = 0

        for index in range(len(s) // 2):
            if s[index] in vowels:
                count += 1

            if s[-index - 1] in vowels:
                count -= 1

        return count == 0
