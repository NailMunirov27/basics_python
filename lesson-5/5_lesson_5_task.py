src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

dict_src = {k: 0 for k in src}
for k in src:
    dict_src[k] += 1

# [23, 1, 3, 10, 4, 11]
print(list(uniq for uniq in dict_src if dict_src[uniq] == 1))
