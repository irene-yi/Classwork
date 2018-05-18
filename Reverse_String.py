def reverse(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

reverse([120, 10, 43, 2, 53, 4, 0, 62, 88, 15, 22, 28, 6, 3, 2, 17, 50, 15, 47])

def rev(str):
    new_str = ""
    for x in new_str:
        new_str = x + new_str
    print(new_str)
rev("tacocat!")
