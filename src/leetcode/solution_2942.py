class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        # results = []
        #
        # for i, v in enumerate(words):
        #     if x in v:
        #         results.append(i)
        #
        # return results
        results = []

        results.extend(i for i, v in enumerate(words) if x in v)
        return results
