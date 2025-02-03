class Solution:
    def convertDateToBinary(self, date: str) -> str:
        new_date = []

        for i in date.split("-"):
            new_date.append(f"{int(i):b}")

        return str("-".join(new_date))
