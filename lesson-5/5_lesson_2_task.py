def my_gen(n):
    list = [a for a in range(1, n + 1, 2)]
    print(*list)

my_gen(13)