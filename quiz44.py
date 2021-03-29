

array = [1, 4, 10]
g = (x for x in array if array.count(x) > 0)
array = [2, 4, 8]
print(list(g))


# [4]