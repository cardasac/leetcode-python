class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangles: list = []

        for i in range(numRows):
            triangles.append([])

            for j in range(i + 1):
                if j in (0, i):
                    triangles[i].append(1)
                else:
                    triangles[i].append(
                        triangles[i - 1][j - 1] + triangles[i - 1][j],
                    )

        return triangles
