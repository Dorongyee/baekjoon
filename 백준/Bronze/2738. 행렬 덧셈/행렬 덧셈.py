row, column = map(int,input().split())
matrix = []
for i in range(row):
    matrix.append(list(map(int, input().split())))

for i in range(row):
    temp_array = list(map(int, input().split()))
    for j in range(column):
        matrix[i][j] += temp_array[j]

for i in range(row):
    for j in range(column):
        print(matrix[i][j],end=' ')
    print()