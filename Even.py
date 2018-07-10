arr1 = ['woof', 'mew', 'bork', 'craww','tricky']
arr2 = ['borf', 'meow', 'growlll', 'chirps', 'tricky']
new_arr = []

i = 0
j = 0

while i < len(arr1):
    if len(arr1[i]) % 2 == 0 and arr1 not in new_arr:
        new_arr.append(arr1[i])
    i = i + 1

    while j < len(arr2):
        if len(arr2[j]) % 2 == 0 and arr2 not in new_arr:
            new_arr.append(arr2[j])
        print(new_arr)
        j = j + 1
