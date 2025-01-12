class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,r=0,len(matrix)-1
        while l<r:
            for i in range(r-l):
                top,bottom=l,r

                #tem value as Topleft
                topleft=matrix[top][l+i]
                #Move bottom Left into top left
                matrix[top][l+i]=matrix[bottom-i][l]
                #move bottom right into bottom left
                matrix[bottom-i][l]=matrix[bottom][r-i]
                #move top right into bottom right
                matrix[bottom][r-i]=matrix[top+i][r]
                #move top right into bottom right
                matrix[top+i][r]=topleft
            l+=1
            r-=1
        