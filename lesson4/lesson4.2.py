def even_index_sum_times_last(lst):
    if not lst:
        return 0

    sum_even_index = 0

    for i in range(0, len(lst), 2):
        sum_even_index += lst[i]

    result = sum_even_index * lst[-1]
    return result

print(even_index_sum_times_last([0, 1, 7, 2, 4, 8]))
print(even_index_sum_times_last([1, 3, 5]))
print(even_index_sum_times_last([6]))
print(even_index_sum_times_last([]))