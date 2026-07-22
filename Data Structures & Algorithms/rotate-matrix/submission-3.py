class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        leng = len(matrix)
        i=0
        while i<leng:
            j=0
            while j<i:
                #swap
                temp = matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp

                j+=1
            i+=1
        for i in range(len(matrix)):
            matrix[i][:] = matrix[i][::-1]

    