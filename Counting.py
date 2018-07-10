def counter (n):
    if n < 1:
        return 0
    else:
        print (n)
        counter(n-1)
counter(10)
