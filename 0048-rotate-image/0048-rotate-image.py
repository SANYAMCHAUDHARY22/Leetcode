class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        s = []
        c = 0

        for i in range(len(matrix)-1,-1,-1):
            for j in range(0,len(matrix)):
                s.append(matrix[i][j])
                c = c + 1

        k = 0
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)):
                matrix[j][i] = s[k]
                k = k + 1