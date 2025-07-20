def move_zeros_to_end(lst):
    result = []
    zero_count = 0

    for number in lst:
        if number == 0:
            zero_count += 1
        else:
            result.append(number)

    for i in range(zero_count):
        result.append(0)

    return result

print(move_zeros_to_end([0, 1, 0, 12, 3]))
print(move_zeros_to_end([0]))
print(move_zeros_to_end([1, 0, 13, 0, 0, 0, 5]))
print(move_zeros_to_end([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))
