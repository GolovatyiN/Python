def move_last_to_front(lst):
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + lst[:-1]

print(move_last_to_front([12, 3, 4, 10]))
print(move_last_to_front([1]))
print(move_last_to_front([]))
print(move_last_to_front([12, 3, 4, 10, 8]))