import random

lst = [random.randint(1, 100) for _ in range(random.randint(3, 10))]

result = [lst[0], lst[2], lst[-2]]

print("Initial list:", lst)
print("Result:", result)
