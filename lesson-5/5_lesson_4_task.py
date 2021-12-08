src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [src[val] for val in range(1, len(src)) if src[val] > src[val - 1]]

# result = [12, 44, 4, 10, 78, 123]
print(result)