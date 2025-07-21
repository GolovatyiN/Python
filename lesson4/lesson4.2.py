lst = [0, 1, 7, 2, 4, 8]
sum_even_index = 0
for i in range(0, len(lst), 2):
    sum_even_index += lst[i]
result = sum_even_index * lst[-1] if lst else 0
print(result)

lst = [1, 3, 5]
sum_even_index = 0
for i in range(0, len(lst), 2):
    sum_even_index += lst[i]
result = sum_even_index * lst[-1] if lst else 0
print(result)

lst = [6]
sum_even_index = 0
for i in range(0, len(lst), 2):
    sum_even_index += lst[i]
result = sum_even_index * lst[-1] if lst else 0
print(result)

lst = []
sum_even_index = 0
for i in range(0, len(lst), 2):
    sum_even_index += lst[i]
result = sum_even_index * lst[-1] if lst else 0
print(result)