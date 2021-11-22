cube = []
cube2 = []
sum_cube = 0

for n in range(1, 1000, 2):
    cube.append(n ** 3)

for i, val in enumerate(cube):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        sum_cube += cube[i]

print(sum_cube)

for z in cube:
    cube2.append(z + 17)
sum_cube = 0
for i, val in enumerate(cube2):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        sum_cube += cube2[i]

print(sum_cube)
