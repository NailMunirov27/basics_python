def my_gen(n):
    for i in range(1, n + 1):
        yield i

for a in my_gen(13):
    if a % 2 == 1:
        print(a)


