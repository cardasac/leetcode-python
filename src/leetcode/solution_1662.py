class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return "".join(word1) == "".join(word2)

    # def arrayStringsAreEqual2(
    #     self, word1: List[str], word2: List[str]
    # ) -> bool:
    #     for c1, c2 in zip(self.generate(word1), self.generate(word2)):
    #         if c1 != c2:
    #             return False
    #     return True
    #
    # def generate(self, wordlist: List[str]):
    #     for word in wordlist:
    #         for char in word:
    #             yield char
    #     yield None
