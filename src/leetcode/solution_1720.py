

class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        decoded: list[int] = [first]  # Given the first number, insert it into array.

        # Decoding XOR is just reversing it, do this with every single number.
        decoded.extend(decoded[-1] ^ number for number in encoded)

        return decoded
