def common_elements():
    list1 = [i for i in range(100) if i % 3 == 0]
    list2 = [i for i in range(100) if i % 5 == 0]
    return set(list1) & set(list2)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("ОК")