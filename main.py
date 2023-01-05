#wrapper class for a nxm matrix + util functions
class MATRIX:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        output = ""
        for x in self.matrix:
            for y in x:
                output += str(y)
                output += " "
            output += "\n"
        return output
    def getRow(self,index):
        return self.matrix[index]

    def getColumn(self,index):
        temp = [];
        for x in range(len(self.matrix)):
            temp.append(self.matrix[x][index])
        return temp
    def swapRow(self, index1, index2):
        temp = self.matrix[index1]
        self.matrix[index1] = self.matrix[index2]
        self.matrix[index2] = temp

    def scaleRow(self, index, scaleFactor):
        for x in range(len(self.matrix[index])):
            self.matrix[index][x] = self.matrix[index][x]*scaleFactor

    def synthRow(self, outputIndex, inputIndex, inputScaleFactor):
        # outputRow <-- outputRow + inputScaleFactor*inputRow
        #input row stays unmodified
        for x in range(len(self.matrix[outputIndex])):
            self.matrix[outputIndex][x] = self.matrix[outputIndex][x] + self.matrix[inputIndex][x]*inputScaleFactor

    def checkReducedEchelon(self):
        #checks to see if the matrix is in reduced echelon form (not rref) with all pivot points being 1
        m = self.matrix
        #remove augment
        for x in range(len(m)):
            m[x].pop(len(m[x])-1)

        #checks for steplike structure
        for row in range(len(m)):
            for col in range(len(m[row])):
                if(m[row][col] == 1):
                    for x in range(row+1, len(m)):
                        if self.getColumn(col)[x] != 0:
                            return False;
                    break
            row+=1

        #checks if each leading value is equal to one
        for x in m:
            for y in x:
                if y==1:
                    break;
                elif y!=0:
                    return False;
        return True;

    def checkEchelon(self):
        m = self.matrix
        # remove augment
        for x in range(len(m)):
            m[x].pop(len(m[x]) - 1)

        # checks for steplike structure
        for row in range(len(m)):
            for col in range(len(m[row])):
                if (m[row][col] == 1):
                    for x in range(row + 1, len(m)):
                        if self.getColumn(col)[x] != 0:
                            return False;
                    break
            row += 1

        return True;

def GaussianDecomposition(matrix):
    while(matrix.checkEchelon() == False):
    #Forward Phase: Identify pivot column, leftmost nonzero column

    #Choose largest absolute value number in the column as the pivot

    #Move corresponding row to the top of the matrix

    #Use row replacement algorithm to zero out all other rows

    #Remove completed row from the matrix and recurse on submatrix


m1 = MATRIX([[1,2,3,6],[0,2,2,4],[0,0,0,4]])
print(m1)
print(m1.checkEchelon())
