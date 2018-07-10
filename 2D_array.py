matrix = [['woof', 'mew', 'bork', 'craww','tricky'], ['borf', 'meow', 'growlll', 'chirps', 'tricky']]
new_arr = []

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if len(matrix[x][y]) % 2 != 0 and matrix not in new_arr:
            new_arr.append(matrix[x][y])
print(new_arr)
