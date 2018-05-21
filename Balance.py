def balance(left, right):
    left_value = 0
    right_value = 0

    for i in left:
        if i == "!":
            left_value += 2
        elif i == "?":
            left_value += 3
    for j in right:
        if j == "!":
            right_value += 2
        elif j == "?":
            right_value += 3

    if left_value > right_value:
        return 'Left'
    elif left_value < right_value:
        return 'Right'
    elif left_value == right_value:
        return 'Balance'
