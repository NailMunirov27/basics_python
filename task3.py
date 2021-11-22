# per = int(input("Введи число: "))
for per in range(101):

    if per % 10 == 1  and per % 100 != 11 :
        print(per, ' процент')
# 11- 14
    elif 2 <= per % 10 <= 4 and not 11 <= per <= 15:
        print(per, ' процента')
    else:
        print(per, ' процентов')