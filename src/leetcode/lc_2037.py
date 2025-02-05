class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0

        for i, v in enumerate(students):
            moves += abs(v - seats[i])

        return moves
