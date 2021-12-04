def my_gen(n):
    list = [a for a in range(1, n + 1) if a % 2 == 0]
    print(list)

my_gen(13)