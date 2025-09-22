class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      
        if numRows == 1:
            return [[1]]
        
        output = [[1], [1,1]]

        for i in range(3, numRows+1):
            row = [1]
            for j in range(i - 2):
                row.append(output[i-2][j] + output[i-2][j+1])

            row.append(1)
            output.append(row)

        return output
