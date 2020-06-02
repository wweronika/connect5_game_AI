m = [[ str(i) for i in range(8)] for j in range(8)]

size = 8
winLength = 5

for line in m:
    print(line)

for j in range(size - winLength + 1):
    diagonalString1 = ''.join([m[i+j][i] for i in range(size-j)])
    diagonalString2 = ''.join([m[i][i+j] for i in range(size-j)])
    print(diagonalString1, diagonalString2)

