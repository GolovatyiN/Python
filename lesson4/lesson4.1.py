lst = [0, 1, 0, 12, 3]
non_zeros = [x for x in lst if x != 0]
zeros = [0] * (len(lst) - len(non_zeros))
lst[:] = non_zeros + zeros
print(lst)

lst = [0]
non_zeros = [x for x in lst if x != 0]
zeros = [0] * (len(lst) - len(non_zeros))
lst[:] = non_zeros + zeros
print(lst)

lst = [1, 0, 13, 0, 0, 0, 5]
non_zeros = [x for x in lst if x != 0]
zeros = [0] * (len(lst) - len(non_zeros))
lst[:] = non_zeros + zeros
print(lst)

lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
non_zeros = [x for x in lst if x != 0]
zeros = [0] * (len(lst) - len(non_zeros))
lst[:] = non_zeros + zeros
print(lst)
