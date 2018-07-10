matrix = [[60, 90, 75], [20, 40, 30], [50, 80, 65], [40, 60, 70], [90, 100, 80], [101, 87, 94], [82, 58, 42]]
high_temp = 0

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] > high_temp:
            high_temp = matrix [x] [y]
print(high_temp)
