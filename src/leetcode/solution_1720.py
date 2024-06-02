from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded: List[int] = [first]  # Given the first number, insert it into array.

        # Decoding XOR is just reversing it, do this with every single number.
        for number in encoded:
            decoded.append(decoded[-1] ^ number)

        return decoded
