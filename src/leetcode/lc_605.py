class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        if len(flowerbed) < 2 and 1 in flowerbed:
            return False

        if n == 1 and len(flowerbed) == 1:
            return True

        result = 0

        for i, v in enumerate(flowerbed):
            if result == n:
                return True

            if i == 0 and v == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                result += 1
                continue

            if i == len(flowerbed) - 1 and v == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                result += 1
                break

            if i == len(flowerbed) - 1:
                break

            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and v == 0:
                result += 1
                flowerbed[i] = 1

        return result == n
